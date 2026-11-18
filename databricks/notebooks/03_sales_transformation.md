# Sales Transformation Notebook

## Objective

Prepare sales data for analytics.

### Transformations

- Remove negative amounts
- Validate transaction IDs
- Standardize data types

### PySpark

```python
from pyspark.sql.functions import col

sales_clean = sales.filter(
    col("amount") > 0
)
```

### Output

Validated sales dataset.