CREATE TABLE DimCustomer
(
    CustomerKey INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    City VARCHAR(100),
    State VARCHAR(100)
);

CREATE TABLE DimDate
(
    DateKey INT PRIMARY KEY,
    DateValue DATE,
    MonthName VARCHAR(20),
    YearNumber INT
);

CREATE TABLE FactSales
(
    SalesKey INT PRIMARY KEY,
    CustomerKey INT,
    ProductKey INT,
    DateKey INT,
    Amount DECIMAL(10,2),
    Quantity INT
);