# Change Data Capture (CDC)

## Overview

This project implements Change Data Capture (CDC) patterns to process only new or modified records, reducing execution times and minimizing unnecessary data movement.

The solution supports:

- Full Loads
- Incremental Loads
- Watermark-Based Loading
- Late Arriving Data Handling
- Duplicate Prevention
- Failed Load Recovery

---

# Business Problem

Loading an entire dataset every day creates:

- Long pipeline execution times
- Increased storage consumption
- Duplicate records
- Higher compute costs

Instead, CDC processes only records that changed since the previous execution.

---

# Source Dataset

Customers

| CustomerID | Name | LastModified |
|------------|------------|------------|
| 1 | Hugo | 2026-01-01 |
| 2 | Ana | 2026-01-02 |
| 3 | John | 2026-01-03 |

---

# CDC Strategy

The CDC process uses the LastModified column.

## Previous Load

```text
2026-01-02 00:00:00
```

## Current Query

```sql
SELECT *
FROM Customers
WHERE LastModified >
      @LastLoadDate
```

Only modified records are extracted.

---

# Full Load

## Usage

Executed:

- Initial deployment
- Recovery scenarios
- Historical reconstruction

## Process

Source System
    ↓
Full Extract
    ↓
ADLS Raw
    ↓
Transform
    ↓
Data Warehouse

Example:

```sql
SELECT *
FROM Customers;
```

---

# Incremental Load

## Usage

Executed daily.

Only records modified after the previous execution are processed.

## Process

Source System
     ↓
Incremental Query
     ↓
ADLS Raw
     ↓
Transform
     ↓
Warehouse Update

Example:

```sql
SELECT *
FROM Customers
WHERE LastModified >
      @LastLoadDate
```

---

# Watermark Strategy

A watermark stores the timestamp of the last successful execution.

Example control table:

```sql
CREATE TABLE ETL_Control
(
    PipelineName VARCHAR(100),
    LastLoadDate DATETIME
);
```

Example:

| Pipeline | LastLoadDate |
|-----------|-------------|
| Customers | 2026-01-02 |

After a successful load:

```sql
UPDATE ETL_Control
SET LastLoadDate = GETDATE()
WHERE PipelineName='Customers';
```

---

# Late Arriving Data

Scenario:

A record modified yesterday arrives today.

Solution:

Use a lookback window.

```sql
SELECT *
FROM Customers
WHERE LastModified >
DATEADD(day,-1,@LastLoadDate)
```

This helps avoid missing records.

---

# Duplicate Prevention

Validation rules:

- CustomerID unique