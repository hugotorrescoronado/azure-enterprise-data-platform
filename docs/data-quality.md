# Data Quality Framework

## Overview

This framework validates data quality before data is promoted from the Raw layer to the Curated layer.

The objective is to ensure data integrity, consistency, completeness, and accuracy across all ingestion pipelines.

---

## Data Quality Architecture

Source Systems
|
├── REST APIs
├── CSV Files
├── JSON Files
├── SFTP Files
└── SQL Databases

        ↓

Raw Zone (ADLS Gen2)

        ↓

Data Quality Validation

        ↓

Curated Zone

        ↓

Data Warehouse / Lakehouse

---

## Validation Categories

### 1. Null Validation

Purpose:

Ensure mandatory columns contain values.

Checks:

- CustomerID cannot be null
- OrderID cannot be null
- LastModifiedDate cannot be null

Example:

| Column | Rule |
|----------|----------|
| customer_id | NOT NULL |
| order_id | NOT NULL |
| last_modified | NOT NULL |

Python Example:

```python
assert df["customer_id"].isnull().sum() == 0
```

---

### 2. Duplicate Validation

Purpose:

Prevent duplicate records from entering analytical systems.

Checks:

- Duplicate customer IDs
- Duplicate order IDs
- Duplicate transactions

Python Example:

```python
duplicates = df.duplicated().sum()

assert duplicates == 0
```

---

### 3. Data Type Validation

Purpose:

Ensure columns contain valid values.

Examples:

| Column | Expected Type |
|----------|----------|
| customer_id | Integer |
| amount | Decimal |
| order_date | Date |
| city | String |

Python Example:

```python
df["customer_id"] = df["customer_id"].astype(int)
```

---

### 4. Business Rule Validation

Purpose:

Validate business-specific requirements.

Examples:

| Rule | Expected Result |
|---------|---------|
| Amount > 0 | True |
| Customer Exists | True |
| Order Date <= Today | True |

Python Example:

```python
assert (df["amount"] > 0).all()
```

---

### 5. Schema Validation

Purpose:

Detect unexpected schema changes.

Checks:

- Missing columns
- New columns
- Data type changes

Expected Schema:

```text
customer_id
name
city
last_modified
```

---

### 6. Referential Integrity Validation

Purpose:

Validate relationships between datasets.

Examples:

FactSales.CustomerKey
must exist in
DimCustomer.CustomerKey

SQL Example:

```sql
SELECT *
FROM FactSales fs
LEFT JOIN DimCustomer dc
     ON fs.CustomerKey =
        dc.CustomerKey
WHERE dc.CustomerKey IS NULL
```

---

### 7. Data Freshness Validation

Purpose:

Ensure data has been loaded recently.

Checks:

- Last successful load timestamp
- Pipeline execution timestamp
- Maximum age threshold

Example:

```sql
SELECT MAX(last_modified)
FROM customers
```

---

## Error Handling Strategy

If validation fails:

1. Pipeline stops.
2. Invalid records are quarantined.
3. Error is logged.
4. Notification is generated.
5. Data Engineering team investigates.

---

## Metrics

The framework tracks:

- Total Records
- Valid Records
- Invalid Records
- Duplicate Records
- Completeness %
- Accuracy %
- Data Freshness
- Pipeline Success Rate

---

## Future Enhancements

- Great Expectations
- Azure Data Factory Validation Activities
- Azure Data Quality Monitoring
- Microsoft Fabric Data Quality Reports