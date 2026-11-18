from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.getOrCreate()

sales = spark.read.csv(
    "../datasets/orders.csv",
    header=True
)

sales = sales.filter(
    col("amount") > 0
)

sales.write.mode("overwrite").parquet(
    "../adls/curated/orders"
)