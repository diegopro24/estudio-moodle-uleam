# Acceso móvil al aula virtual Moodle – ULEAM

Repositorio de evidencias de la Fase 3 del proyecto *Optimización del Acceso Móvil al Aula Virtual Moodle en la ULEAM mediante una Arquitectura Cliente-Servidor Orientada a Móviles*.

Autores: Milena Vacacela, Jeremy Taipe y Diego Cedeño. Ingeniería en Software, ULEAM Extensión El Carmen.

## Estado de los datos

| Elemento | Estado |
|---|---|
| Instrumento (Google Forms) | Elaborado |
| Recolección de datos reales | **En curso** (fechas y N se actualizarán al cerrar) |
| `datos_sinteticos_PRUEBA.csv` | **Datos sintéticos NO reales**, solo para probar el script |
| Respuestas reales anonimizadas | Pendiente: se subirán al terminar la recolección |

> Los datos sintéticos no representan a ningún 

## Archivos

- `generar_datos_sinteticos.py`: genera datos de prueba (no reales).
- `analisis.py`: análisis descriptivo (frecuencias, porcentajes, medias).
- `datos_sinteticos_PRUEBA.csv`: datos de prueba generados con el script anterior.

## Cómo reproducir

```bash
pip install pandas
python analisis.py datos_sinteticos_PRUEBA.csv
```

Para los datos reales, ejecutar `python analisis.py` con el CSV de respuestas anonimizadas.

## Anonimización

No se recopilaron nombres, correos ni cédulas. La marca temporal se elimina del CSV antes de publicarlo.

## Licencia

Datos: CC-BY 4.0. Scripts: MIT.
