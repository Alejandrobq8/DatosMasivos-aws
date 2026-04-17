# DatosMasivos-AWS 🐦

Análisis de sentimientos de tweets a gran escala usando servicios de AWS y Google Colab.

---

## 📌 Descripción

Este proyecto implementa un pipeline de datos completo para procesar y analizar
sentimientos en tweets, utilizando el dataset de Kaggle
**Sentiment140 (1.6 millones de tweets)**.

---

## 🏗️ Arquitectura

![Diagrama de Arquitectura](docs/arquitectura.png)

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
│   ├── create_table_tweets_db.sql
│   ├── tweet_activity_by_hour_and_day.sql
│   ├── user_sentiment_analysis.sql
│   ├── hashtag_frequency_sentiment.sql
│   └── total_tweets.sql
├── data/
│   └── raw/               # No incluido en el repo (archivos pesados)
├── iam/
│   └── policies.json
├── notebooks/
│   └── visualizaciones.ipynb
├── scripts/
│   └── etl_lambda.py
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Cómo reproducir el proyecto

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/DatosMasivos-aws.git
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

### 4. Descargar dataset de Kaggle
- Dataset: [Sentiment140](https://www.kaggle.com/datasets/kazanova/sentiment140)
- Colocar en: `data/raw/raw/`

### 5. Ejecutar queries en Athena
- Ejecutar primero `create_database.sql`
- Luego `create_table_tweets_db.sql`
- Finalmente los queries de análisis

### 6. Ver visualizaciones
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tu-usuario/DatosMasivos-aws/blob/main/notebooks/visualizaciones.ipynb)

---

## 📊 Análisis incluidos

- **Actividad por hora y día** — ¿Cuándo tuitea más la gente?
- **Sentimiento por usuario** — Top usuarios positivos y negativos
- **Hashtags más frecuentes** — Tendencias y su polaridad
- **Total de tweets** — Resumen general del dataset

---

## ⚠️ Pendiente
- [ ] Acceso a bucket S3 para descarga de datos procesados
- [ ] Exportar dashboards finales desde Google Colab

---

## 👥 Equipo
- Desarrollo del pipeline AWS: _[nombre del compañero]_
- Análisis y consultas SQL: _[tu nombre]_