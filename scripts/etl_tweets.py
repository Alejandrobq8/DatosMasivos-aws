import boto3
import pandas as pd
import io
import os
import pyarrow as pa
import pyarrow.parquet as pq
from datetime import datetime

s3 = boto3.client('s3')

SOURCE_BUCKET = 'datos-masivos-ulacit-2026v'
SOURCE_KEY    = 'raw/training.1600000.processed.noemoticon.csv'
DEST_BUCKET   = 'datos-masivos-ulacit-2026v'
DEST_PREFIX   = 'processed/'

COLUMN_MAP = {
    'target': 'target',
    'ids':    'id',
    'date':   'date',
    'flag':   'flag',
    'user':   'user',
    'text':   'text',
}

def lambda_handler(event, context):
    print("Iniciando ETL...")

    response = s3.get_object(Bucket=SOURCE_BUCKET, Key=SOURCE_KEY)
    raw_data = response['Body'].read()

    writer = None
    total_filas = 0

    for chunk in pd.read_csv(
        io.BytesIO(raw_data),
        chunksize=50_000,
        encoding='latin-1',
        header=None,
        names=list(COLUMN_MAP.keys())
    ):
        chunk.dropna(inplace=True)
        chunk.drop_duplicates(inplace=True)
        chunk.rename(columns=COLUMN_MAP, inplace=True)

        chunk['date'] = pd.to_datetime(
            chunk['date'],
            format='%a %b %d %H:%M:%S PDT %Y',
            errors='coerce'
        )
        chunk.dropna(subset=['date'], inplace=True)

        chunk['hour']        = chunk['date'].dt.hour
        chunk['day_of_week'] = chunk['date'].dt.day_name()
        chunk['polarity']    = (chunk['target'] == 4).astype(int)
        chunk['date']        = chunk['date'].dt.strftime('%Y-%m-%d %H:%M:%S')

        table = pa.Table.from_pandas(chunk, preserve_index=False)

        if writer is None:
            writer = pq.ParquetWriter(
                '/tmp/output.parquet',
                table.schema
            )

        writer.write_table(table)
        total_filas += len(chunk)
        print(f"Chunk procesado: {len(chunk)} filas — total: {total_filas}")

    if writer:
        writer.close()

    # Subir el archivo final a S3
    output_key = f"{DEST_PREFIX}tweets_processed.parquet"
    s3.upload_file('/tmp/output.parquet', DEST_BUCKET, output_key)

    print(f"Guardado en s3://{DEST_BUCKET}/{output_key}")
    return {
        'statusCode': 200,
        'body': f'ETL completado. Filas: {total_filas}'
    }