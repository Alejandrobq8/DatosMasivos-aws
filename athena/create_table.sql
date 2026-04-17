CREATE EXTERNAL TABLE IF NOT EXISTS tweets_db.tweets ( target INT, id BIGINT, date STRING, flag STRING, user STRING, text STRING, hour INT, day_of_week STRING, polarity INT
)
STORED AS PARQUET
LOCATION 's3://datos-masivos-ulacit-2026v/processed/'
TBLPROPERTIES ('parquet.compress'='SNAPPY')