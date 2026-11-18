from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    current_timestamp
)

spark = SparkSession.builder \
    .appName("CustomerValidation") \
    .getOrCreate()

customers = spark.read.csv(
    "../datasets/customers.csv",
    header=True,
    inferSchema=True
)

# Rule 1
valid_customer_id = customers.filter(
    col("customer_id").isNotNull()
)

# Rule 2
valid_name = valid_customer_id.filter(
    col("name").isNotNull()
)

# Rule 3
valid_city = valid_name.filter(
    col("city").isNotNull()
)

# Remove duplicates
validated = valid_city.dropDuplicates()

validated = validated.withColumn(
    "validation_timestamp",
    current_timestamp()
)

validated.write.mode(
    "overwrite"
).parquet(
    "../adls/curated/customers_validated"
)

print("Validation Successful")

spark.stop()