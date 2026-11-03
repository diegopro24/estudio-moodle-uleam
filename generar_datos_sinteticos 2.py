"""
GENERA DATOS SINTETICOS DE PRUEBA. NO SON RESPUESTAS REALES.
Solo sirven para probar que analisis.py funciona mientras se recolectan los datos reales.
"""
import random
import pandas as pd

random.seed(42)
N = 30
FREC = ["Nunca", "Casi Nunca", "A veces", "Casi Siempre", "Siempre"]
ACU = ["Nada de acuerdo", "Poco de acuerdo", "Más o menos de acuerdo", "De acuerdo", "Totalmente de acuerdo"]
MOT = ["No supe configurarla porque pide escribir la dirección del sitio de la universidad",
       "No pude iniciar sesión", "Me pareció complicada",
       "Prefiero entrar desde Chrome (google), Safari u otro", "Otra razón", "No aplica"]
FAL = ["Falló al subir el archivo", "No me avisaron", "No vi cuánto plazo quedaba", "Ninguna, nunca me pasó"]

filas = []
for _ in range(N):
    filas.append({
        "entrega": random.choice(["El celular", "La computadora", "Los dos por igual"]),
        "acceso": random.choice(["Escribo o abro la página de la universidad desde Chrome (Google), Safari u otro programa de internet",
                                 "Uso la aplicación de Moodle (la que se descarga de la tienda de aplicaciones)",
                                 "Uso las dos formas", "No entro desde el celular"]),
        "conoce_app": random.choice(["Si", "No"]),
        "uso_app": random.choice(["Nunca la he usado / No la descargué", "La instalé y la sigo usando", "La instalé y la dejé de usar"]),
        "motivos": ", ".join(random.sample(MOT, random.randint(1, 2))),
        **{f"c{i}": random.choice(FREC) for i in range(1, 5)},
        "enterarse": random.choice(["Entro a revisar por mi cuenta", "Me llega un aviso al celular",
                                    "Me entero tarde o no me entero", "Me avisan mis compañeros o por WhatsApp"]),
        "fallas": ", ".join(random.sample(FAL, random.randint(1, 2))),
        "d1": random.choice(ACU),
        "origen": "SINTETICO_NO_REAL",
    })

pd.DataFrame(filas).to_csv("datos_sinteticos_PRUEBA.csv", index=False)
print("Generado: datos_sinteticos_PRUEBA.csv (DATOS NO REALES)")
