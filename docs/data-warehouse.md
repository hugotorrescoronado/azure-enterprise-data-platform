# Enterprise Data Warehouse

## Overview

Enterprise Data Warehouse used for reporting,
analytics and business intelligence.

---

## Architecture

Source Systems
        ↓
Azure Data Factory
        ↓
ADLS Gen2
        ↓
Data Warehouse
        ↓
Power BI

---

## Fact Tables

Fact tables contain business events and measures.

### FactSales

| Column | Description |
|----------|----------|
| SalesKey | Transaction identifier |
| CustomerKey | Customer reference |
| ProductKey | Product reference |
| DateKey | Date reference |
| Amount | Revenue amount |
| Quantity | Units sold |

See:

```text
sql/create_datawarehouse.sql
```

---

## Dimension Tables

Dimension tables contain descriptive attributes.

### DimCustomer

| Column | Description |
|----------|----------|
| CustomerKey | Business key |
| CustomerName | Customer name |
| City | Customer city |
| State | Customer state |

---

## Stored Procedures

Stored procedures are used to standardize
loading processes.

Example:

sp_LoadCustomers

Benefits:

- Reusability
- Better governance
- Reduced maintenance

---

## Complex Joins

Used to combine information from fact and
dimension tables.

Example:

See:

sql/advanced_queries.sql

---

## Common Table Expressions (CTEs)

Used to simplify complex transformations and
reporting queries.

Example:

WITH SalesCTE AS (...)

---

## Window Functions

Used for ranking and analytical calculations.

Examples:

- ROW_NUMBER()
- RANK()
- DENSE_RANK()
- SUM OVER()

---

## Query Optimization

Techniques:

- Clustered indexes
- Nonclustered indexes
- Execution plans
- Statistics

Example:

CREATE INDEX idx_customer
ON FactSales(CustomerKey);

---

## Dimensional Modeling

Star Schema:

FactSales
    |
-------------------
|        |        |
▼        ▼        ▼
Customer Product Date

---

## Data Quality Integration

Before data enters the warehouse:

- Null Validation
- Duplicate Validation
- Type Validation
- Business Rules
- Referential Integrity

---

## Business Intelligence

The warehouse supports:

- Power BI
- Fabric Warehouse
- Fabric Semantic Models
- Executive Dashboards