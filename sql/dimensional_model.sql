/* ===========================
   DIMENSIONS
=========================== */

CREATE TABLE DimCustomer
(
    CustomerKey INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    City VARCHAR(100),
    Country VARCHAR(100)
);

CREATE TABLE DimProduct
(
    ProductKey INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Category VARCHAR(50)
);

CREATE TABLE DimDate
(
    DateKey INT PRIMARY KEY,
    DateValue DATE,
    MonthName VARCHAR(20),
    QuarterNumber INT,
    YearNumber INT
);

/* ===========================
   FACT TABLE
=========================== */

CREATE TABLE FactSales
(
    SalesKey INT PRIMARY KEY,
    CustomerKey INT,
    ProductKey INT,
    DateKey INT,
    Amount DECIMAL(10,2),
    Quantity INT
);