# Parquet Export Notebook

## Objective

Convert datasets into Parquet format.

### PySpark

```python
customers_clean.write \
    .mode("overwrite") \
    .parquet(
        "../adls/curated/customers"
    )
```

### Benefits

- Better compression
- Faster analytics
- Optimized for Fabric and Databricks