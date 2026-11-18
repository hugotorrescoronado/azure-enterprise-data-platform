# Data Quality Validation Notebook

## Objective

Validate data before promotion to Curated zone.

### Rules

- Null Validation
- Duplicate Validation
- Type Validation
- Business Rule Validation

### PySpark

```python
null_customer_ids = customers.filter(
    customers.customer_id.isNull()
).count()
```

### Expected Result

Only compliant records proceed to Curated storage.