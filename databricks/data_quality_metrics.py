from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.read.csv(
    "../datasets/customers.csv",
    header=True
)

metrics = {
    "total_records": df.count(),
    "unique_records": df.dropDuplicates().count()
}

print(metrics)