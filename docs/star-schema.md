# Dimensional Modeling

## Overview

This project uses dimensional modeling techniques commonly used in enterprise Data Warehouses, Lakehouses, Microsoft Fabric Warehouses, and Power BI semantic models.

The design follows the Kimball methodology using Fact and Dimension tables.

---

# Business Scenario

The company wants to analyze:

- Revenue
- Sales Trends
- Customer Behavior
- Product Performance
- Geographic Analysis

The dimensional model enables fast analytical queries and reporting.

---

# Star Schema Architecture

```
                    FactSales

                         |
      -----------------------------------

      |               |               |

      ▼               ▼               ▼

DimCustomer      DimDate      DimProduct
```

---

# Fact Table

Fact tables contain measurable business events.

Examples:

- Orders
- Sales
- Revenue
- Transactions

---

## FactSales

| Column | Description |
|----------|----------|
| SalesKey | Unique transaction |
| CustomerKey | Customer reference |
| ProductKey | Product reference |
| DateKey | Date reference |
| Amount | Revenue amount |
| Quantity | Units sold |

---

## Fact Table Characteristics

Contains:

- Transactions
- Revenue
- Measures
- Metrics
- Numeric Values

Examples:

```text
Sales Amount
Order Quantity
Profit
Discount
Tax
```

---

# Dimension Tables

Dimension tables provide descriptive information.

Examples:

- Customer
- Product
- Date
- Location

---

## DimCustomer

| Column | Description |
|----------|----------|
| CustomerKey | Customer Identifier |
| CustomerName | Customer Name |
| City | Customer City |
| Country | Customer Country |

---

## DimProduct

| Column | Description |
|----------|----------|
| ProductKey | Product Identifier |
| ProductName | Product Name |
| Category | Product Category |

---

## DimDate

| Column | Description |
|----------|----------|
| DateKey | Date Identifier |
| DateValue | Calendar Date |
| MonthName | Month |
| Quarter | Quarter |
| YearNumber | Year |

---

# Relationships

FactSales

```text
CustomerKey → DimCustomer

ProductKey → DimProduct

DateKey → DimDate
```

This design minimizes redundancy while maximizing reporting performance.

---

# Example Query

Revenue by Customer

```sql
SELECT
    c.CustomerName,
    SUM(f.Amount) AS Revenue
FROM FactSales f
INNER JOIN DimCustomer c
    ON f.CustomerKey = c.CustomerKey
GROUP BY c.CustomerName
ORDER BY Revenue DESC;
```

---

# Star Schema Benefits

- Fast Reporting
- Simplified Analytics
- Better 