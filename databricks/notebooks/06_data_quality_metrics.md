# Data Quality Metrics Notebook

## Objective

Generate quality metrics for monitoring.

### Metrics

- Total Records
- Valid Records
- Invalid Records
- Duplicate Records
- Validation Success Rate

### Example

```python
total_records = customers.count()

valid_records = customers.dropDuplicates().count()

quality_score = (
 valid_records / total_records
) * 100
```

### KPI Output

```text
Quality Score: 98%
```