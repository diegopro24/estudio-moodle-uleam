"""
Analisis descriptivo de la encuesta "Acceso movil a Moodle - ULEAM".
Uso:
  python analisis.py datos_sinteticos_PRUEBA.csv     # prueba (datos NO reales)
  python analisis.py respuestas_anonimizadas.csv     # datos reales
El CSV debe tener las 12 columnas de las preguntas en el orden del formulario
(si trae "Marca temporal", el script la ignora).
"""
import os
import sys
import pandas as pd

ruta = sys.argv[1] if len(sys.argv) > 1 else "respuestas_anonimizadas.csv"
df = pd.read_csv(ruta)
if "marca temporal" in str(df.columns[0]).lower():
    df = df.iloc[:, 1:]
df = df.iloc[:, :12]
df.columns = ["entrega", "acceso", "conoce_app", "uso_app", "motivos",
              "c1", "c2", "c3", "c4", "enterarse", "fallas", "d1"]

os.makedirs("resultados", exist_ok=True)
print(f"Archivo: {ruta}\nN valido: {len(df)}\n")

# Preguntas de una sola opcion
for col in ["entrega", "acceso", "conoce_app", "uso_app", "enterarse"]:
    f = df[col].value_counts()
    p = (df[col].value_counts(normalize=True) * 100).round(1)
    out = pd.DataFrame({"frecuencia": f, "porcentaje": p})
    print(col, "\n", out, "\n")
    out.to_csv(f"resultados/frec_{col}.csv")

# Preguntas de seleccion multiple (se cuenta por texto de cada opcion)
def multiple(col, opciones):
    n = len(df)
    filas = {o: int(df[col].astype(str).str.contains(o, regex=False).sum()) for o in opciones}
    out = pd.DataFrame({"frecuencia": filas})
    out["porcentaje"] = (out["frecuencia"] / n * 100).round(1)
    print(col, "\n", out, "\n")
    out.to_csv(f"resultados/frec_{col}.csv")

multiple("motivos", ["No supe configurarla", "No pude iniciar sesión", "Me pareció complicada",
                     "Prefiero entrar desde Chrome", "Otra razón", "No aplica"])
multiple("fallas", ["Falló al subir el archivo", "No me avisaron",
                    "No vi cuánto plazo quedaba", "Ninguna"])

# Pregunta 6 (frecuencia) y pregunta 9 (acuerdo): texto -> 1 a 5
FREC = {"nunca": 1, "casi nunca": 2, "a veces": 3, "casi siempre": 4, "siempre": 5}
ACU = {"nada de acuerdo": 1, "poco de acuerdo": 2, "más o menos de acuerdo": 3,
       "de acuerdo": 4, "totalmente de acuerdo": 5}
for c in ["c1", "c2", "c3", "c4"]:
    df[c] = df[c].astype(str).str.strip().str.lower().map(FREC)
df["d1"] = df["d1"].astype(str).str.strip().str.lower().map(ACU)

cols = ["c1", "c2", "c3", "c4", "d1"]
res = pd.DataFrame({"media": df[cols].mean().round(2),
                    "pct_4_o_5": ((df[cols] >= 4).mean() * 100).round(1)})
print("Escalas (c4 = 'recibo avisos', interpretar en sentido inverso)\n", res)
res.to_csv("resultados/resumen_escalas.csv")
