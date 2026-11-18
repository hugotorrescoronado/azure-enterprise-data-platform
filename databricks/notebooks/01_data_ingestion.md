# Data Ingestion Notebook

## Objective

Ingest customer data from CSV files into Spark DataFrames.

### Source

```text
datasets/customers.csv
```

### PySpark Example

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("DataIngestion") \
    .getOrCreate()

customers = spark.read.csv(
    "../datasets/customers.csv",
    header=True,
    inferSchema=True
)

customers.show()
```

### Output

Spark DataFrame ready for transformation.