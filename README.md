# DatosMasivos-AWS 🐦

Análisis de sentimientos de tweets a gran escala usando servicios de AWS y Google Colab.

---

## 📌 Descripción

Este proyecto implementa un pipeline de datos completo para procesar y analizar
sentimientos en tweets, utilizando el dataset de Kaggle
**Sentiment140 (1.6 millones de tweets)**.

---

## 📦 Dataset

| Campo | Detalle |
|-------|---------|
| Nombre | Sentiment140 |
| Fuente | Kaggle |
| Enlace | https://www.kaggle.com/datasets/kazanova/sentiment140 |
| Tamaño | 227 MB |
| Formato | CSV |
| Registros | 1,600,000 tweets |
| Variables | target, id, date, flag, user, text |

---

## ❓ Preguntas Analíticas

1. ¿En qué hora y día de la semana se genera más actividad en Twitter?
2. ¿Qué usuarios tienen mayor cantidad de tweets y cuál es su polaridad?
3. ¿Cuáles son los hashtags más frecuentes y cuál es su sentimiento promedio?

---

## 🏗️ Arquitectura

| Capa | Servicio | Descripción |
|------|----------|-------------|
| Ingesta | AWS S3 | Almacenamiento de datos crudos y procesados |
| ETL | AWS Lambda | Limpieza, filtrado y transformación de datos |
| Catálogo | AWS Glue | Catalogación de datos para consultas |
| Consultas | Amazon Athena | Análisis SQL sobre los datos procesados |
| Visualización | Google Colab | Métricas, gráficas e insights |
| Seguridad | AWS IAM | Políticas y roles de acceso |

---

## 📁 Estructura del Repositorio

```
DatosMasivos-aws/
├── athena/
│   ├── create_database.sql
│   ├── create_table.sql
│   ├── tweet_activity_by_hour_and_day_of_week.sql
│   ├── user_sentiment_analysis.sql
│   ├── hashtag_frequency_sentiment.sql
│   └── total_tweets.sql
├── data/                  # No incluido en el repo (archivos pesados)
├── iam/
│   └── policies.json
├── notebooks/
│   └── visualizaciones.ipynb
├── scripts/
│   └── etl_tweets.py
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Cómo reproducir el proyecto

### 1. Clonar el repositorio
```bash
git clone https://github.com/Alejandrobq8/DatosMasivos-aws.git
cd DatosMasivos-aws
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Configurar credenciales AWS
```bash
aws configure
```

### 4. Descargar dataset desde S3
```bash
aws s3 cp s3://datos-masivos-ulacit-2026v/raw/ ./data/raw/raw/ --recursive
aws s3 cp s3://datos-masivos-ulacit-2026v/processed/ ./data/raw/processed/ --recursive
```

### 5. Ejecutar queries en Athena
- Ejecutar primero `create_database.sql`
- Luego `create_table.sql`
- Finalmente los queries de análisis

### 6. Ver visualizaciones
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Alejandrobq8/DatosMasivos-aws/blob/main/notebooks/visualizaciones.ipynb)

---

## 📊 Análisis incluidos

- **Actividad por hora y día** — ¿Cuándo tuitea más la gente?
- **Sentimiento por usuario** — Top usuarios positivos y negativos
- **Hashtags más frecuentes** — Tendencias y su polaridad
- **Total de tweets** — Resumen general del dataset

---