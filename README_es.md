# Benchmarking_test
---

[![OSA-improved](https://img.shields.io/badge/improved%20by-OSA-yellow)](https://github.com/aimclub/OSA)

Built with:

![numpy](https://img.shields.io/badge/NumPy-013243.svg?style={0}&logo=NumPy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458.svg?style={0}&logo=pandas&logoColor=white)
![scipy](https://img.shields.io/badge/SciPy-8CAAE6.svg?style={0}&logo=SciPy&logoColor=white)
![tqdm](https://img.shields.io/badge/tqdm-FFC107.svg?style={0}&logo=tqdm&logoColor=black)

---

## Visión general

Benchmarking_test capacita a los equipos para descubrir y abordar fallas ocultas en modelos predictivos mediante la creación automática de pruebas de casos extremos realistas. Destaca brechas de precisión, sesgos y problemas de robustez, permitiendo una mejora de modelos más rápida y justa sin etiquetado manual.

---

## Tabla de contenidos

- [Visión general](#overview)
- [Características principales](#core-features)
- [Instalación](#installation)
- [Contribuciones](#contributing)
- [Citación](#citation)

---

## Características principales

1. **Preprocesamiento de datos y Ingeniería de características**: Limpieza, codificación, escalado y descomposición de fechas de conjuntos de datos de apartamentos y series temporales en bruto, eliminando columnas irrelevantes y ordenando las observaciones cronológicamente para preparar los datos para el modelado posterior.
2. **Suite de entrenamiento de modelos de regresión**: Entrenamiento y evaluación de múltiples algoritmos de regresión (KNN, Gradient Boosting, Random Forest, XGBoost, Regresión Lineal) en datos de precios inmobiliarios con persistencia y reporte de rendimiento automáticos (R², MAPE).
3. **Pipeline de benchmarking generativo de dos etapas**: Combina algoritmos genéticos para identificar instancias mal predichas con autoencoders variacionales que aprenden la distribución de casos de fallo, produciendo ejemplos de prueba sintéticos que apuntan a las debilidades del modelo.
4. **Generación de escenarios conscientes de la equidad**: Crea ejemplos sintéticos contrafactuales en subespacios de características con bajo rendimiento para exponer y mitigar sesgos en segmentos demográficos y geográficos.
5. **Generación de datos sintéticos para casos extremos**: Genera muestras sintéticas de alta densidad en regiones del espacio de características donde los modelos presentan altos errores, facilitando pruebas robustas y mejora continua.

---

## Instalación

Instala Benchmarking_test usando uno de los siguientes métodos:

**Construir desde la fuente:**

1. Clona el repositorio Benchmarking_test:
   ```sh
   git clone https://github.com/fl1pcoin/Benchmarking_test
   ```
2. Navega al directorio del proyecto:
   ```sh
   cd Benchmarking_test
   ```
3. Instala las dependencias del proyecto:
   ```sh
   pip install -r requirements.txt
   ```

---

## Contribuciones

- **[Reportar problemas](https://github.com/fl1pcoin/Benchmarking_test/issues)**: Envía errores encontrados o registra solicitudes de funciones para el proyecto.
- **[Enviar Pull Requests](https://github.com/fl1pcoin/Benchmarking_test/tree/experiments/.github/CONTRIBUTING.md)**: Para aprender más sobre cómo contribuir a Benchmarking_test.

---

## Citación

DRMPN (2025). Repositorio Benchmarking [Software de computadora]. https://github.com/DRMPN/Benchmarking

```bibtex
@misc{Benchmarking,
    author = {DRMPN},
    title = {Benchmarking repository},
    year = {2025},
    publisher = {github.com},
    journal = {github.com repository},
    howpublished = {\url{https://github.com/DRMPN/Benchmarking.git}},
    url = {https://github.com/DRMPN/Benchmarking.git}
}
```
