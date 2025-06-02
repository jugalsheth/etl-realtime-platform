from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
import pandas as pd
import os

# 1. Create Spark session
spark = SparkSession.builder \
    .appName("KafkaOrderConsumer") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.13:4.0.0") \
    .getOrCreate()

# 2. Define schema
schema = StructType([
    StructField("order_id", IntegerType()),
    StructField("item_id", StringType()),
    StructField("qty", IntegerType()),
    StructField("timestamp", StringType())
])

# 3. Read Kafka stream
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "orders_stream") \
    .load()

# 4. Parse Kafka value
orders_df = df.selectExpr("CAST(value AS STRING) as json") \
    .select(from_json(col("json"), schema).alias("data")) \
    .select("data.*")

# 5. Write each micro-batch to CSV
def process_batch(batch_df, batch_id):
    print(f"📦 Processing batch: {batch_id}")
    if batch_df.count() == 0:
        return
    batch_df_pd = batch_df.toPandas()
    file_path = "data/orders_log.csv"
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(file_path):
        batch_df_pd.to_csv(file_path, index=False)
    else:
        batch_df_pd.to_csv(file_path, mode='a', index=False, header=False)

# 6. Start streaming
query = orders_df.writeStream \
    .foreachBatch(process_batch) \
    .option("checkpointLocation", "./checkpoints/orders_stream") \
    .start()

query.awaitTermination()
