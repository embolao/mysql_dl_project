# Proyecto: MySQL Deep Learning Pipeline

Este proyecto implementa un flujo de trabajo modular y reproducible para el entrenamiento, evaluación y gestión de modelos de machine learning utilizando datos almacenados en una base de datos MySQL. Está construido sobre PyScaffold e incluye soporte para modelos en PyTorch y Scikit-learn, además de una interfaz de línea de comandos (CLI), logging estructurado, y almacenamiento automático de resultados.

---

## Estructura del Proyecto

mysql_dl_project/
├── cli.py # Interfaz de línea de comandos
├── init_db.py # Inicialización de la base de datos
├── sql_runner.py # Ejecución de SQLs
├── utils/
│ └── logging.py # Registro de logs en archivos con timestamp
├── ml/
│ ├── init.py
│ ├── db.py # Funciones para cargar datos desde MySQL
│ ├── pipeline.py # Pipeline de procesamiento general
│ ├── pytorch_model.py # Modelo y entrenamiento con PyTorch
│ └── sklearn_model.py # Modelo y entrenamiento con Scikit-learn
outputs/
├── *.png, *.txt, *.pt, .pkl # Archivos generados automáticamente
tests/
└── test_.py # Tests unitarios


---

## Requisitos

- Python 3.12+
- MySQL Server
- Docker (opcional, para pruebas)
- Recomendado: entorno virtual y uso de `pre-commit`

Instalación de dependencias:

```bash
pip install -r requirements.txt
pre-commit install

Uso de la Interfaz CLI
Inicializar la base de datos

mysqlcli init-db

Ejecutar predicción y entrenamiento con Scikit-learn

mysqlcli train-sklearn

Ejecutar predicción y entrenamiento con PyTorch

mysqlcli train-torch

Ver logs generados

mysqlcli view-logs

Funcionalidades Incluidas

    ✔️ Modelos de ML con PyTorch y Scikit-learn

    ✔️ Registro automático de logs con timestamp

    ✔️ Guardado de predicciones, métricas y visualizaciones en outputs/

    ✔️ Modularidad completa para escalabilidad

    ✔️ Tests unitarios con PyTest (tests/)

    ✔️ Integración con pre-commit para estilo y limpieza automática

    ✔️ CLI extensible basada en click

    ✔️ Docker + MySQL de ejemplo en docker-compose.yml

Logs y Salida

Todos los logs y resultados son guardados con marca de tiempo (YYYY-MM-DD_HH-MM-SS) en la carpeta outputs/. Ejemplos:

    outputs/train_torch_log.txt

    outputs/predictions_torch_log.txt

    outputs/loss_torch.png

    outputs/model_torch.pt

    outputs/model_sklearn.pkl

Cómo correr los tests

pytest

Autores y Licencia

Este proyecto fue desarrollado por [embolao].
Licencia: MIT
