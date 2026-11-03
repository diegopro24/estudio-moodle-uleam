"""
Analisis descriptivo de la encuesta.
Uso:
  python scripts/analisis.py                                   # datos reales
  python scripts/analisis.py data/synthetic/datos_sinteticos_PRUEBA.csv   # prueba
Columnas esperadas: carrera, so, acceso, uso_app, motivos, c1..c4, d1..d3
"""
import os
import sys
import pandas as pd

ruta = sys.argv[1] if len(sys.argv) > 1 else "data/raw/respuestas_anonimizadas.csv"
df = pd.read_csv(ruta)
os.makedirs("data/processed", exist_ok=True)
print(f"Archivo: {ruta}\nN válido: {len(df)}\n")

# Frecuencias y porcentajes
for col in ["carrera", "so", "acceso", "uso_app"]:
    f = df[col].value_counts()
    p = (df[col].value_counts(normalize=True) * 100).round(1)
    out = pd.DataFrame({"frecuencia": f, "porcentaje": p})
    print(col, "\n", out, "\n")
    out.to_csv(f"data/processed/frec_{col}.csv")

# Motivos de abandono (selección múltiple)
mot = df["motivos"].str.split(", ").explode().value_counts()
print("motivos\n", mot, "\n")
mot.to_csv("data/processed/frec_motivos.csv")

# Problemas (c) y necesidad percibida (d): media y % que responde 4 o 5
cols = [c for c in df.columns if c[0] in "cd" and c[1:].isdigit()]
res = pd.DataFrame({"media": df[cols].mean().round(2),
                    "pct_4_o_5": ((df[cols] >= 4).mean() * 100).round(1)})
print(res)
res.to_csv("data/processed/resumen_likert.csv")
