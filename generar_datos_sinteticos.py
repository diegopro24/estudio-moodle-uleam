"""
GENERA DATOS SINTETICOS DE PRUEBA. NO SON RESPUESTAS REALES.
Solo sirven para probar que analisis.py funciona mientras se recolectan los datos reales.
"""
import os
import random
import pandas as pd

random.seed(42)
N = 30

carreras = ["Software", "Finanzas", "Auditoría", "Educación", "Enfermería",
            "Fisioterapia", "Agropecuaria / Agronegocios", "Psicología", "Otras"]
motivos = ["No supe configurar la URL del servidor", "No pude iniciar sesión",
           "Es lenta o confusa", "Prefiero el navegador", "No aplica"]

filas = []
for _ in range(N):
    filas.append({
        "carrera": random.choice(carreras),
        "so": random.choice(["Android", "iOS", "Otro"]),
        "acceso": random.choice(["Navegador del celular", "App oficial de Moodle", "Computadora"]),
        "uso_app": random.choice(["Nunca la he usado", "La instalé y la sigo usando",
                                  "La instalé y la dejé de usar"]),
        "motivos": ", ".join(random.sample(motivos, random.randint(1, 2))),
        **{f"c{i}": random.randint(1, 5) for i in range(1, 5)},
        **{f"d{i}": random.randint(1, 5) for i in range(1, 4)},
        "origen": "SINTETICO_NO_REAL",
    })

os.makedirs("data/synthetic", exist_ok=True)
pd.DataFrame(filas).to_csv("data/synthetic/datos_sinteticos_PRUEBA.csv", index=False)
print("Generado: data/synthetic/datos_sinteticos_PRUEBA.csv (DATOS NO REALES)")
