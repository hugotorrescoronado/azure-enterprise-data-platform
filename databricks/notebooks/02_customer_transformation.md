# Customer Transformation Notebook

## Objective

Standardize customer information.

### Transformations

- Uppercase names
- Remove duplicate customers
- Validate mandatory columns

### PySpark

```python
from pyspark.sql.functions import upper

customers_clean = customers \
    .dropDuplicates() \
    .withColumn(
        "name",
        upper(customers["name"])
    )
```

### Output

Curated customer dataset.