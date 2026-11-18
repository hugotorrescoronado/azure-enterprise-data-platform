from pyspark.sql import SparkSession
from pyspark.sql.functions import upper

spark = SparkSession.builder \
    .appName("CustomerTransform") \
    .getOrCreate()

customers = spark.read.csv(
    "../datasets/customers.csv",
    header=True
)

customers_clean = customers \
    .dropDuplicates() \
    .withColumn(
        "name",
        upper(customers["name"])
    )

customers_clean.write \
    .mode("overwrite") \
    .parquet(
        "../adls/curated/customers"
    )