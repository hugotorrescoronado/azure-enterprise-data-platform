/* COMPLEX JOIN */

SELECT
    c.CustomerName,
    SUM(f.Amount) AS TotalSales
FROM FactSales f
INNER JOIN DimCustomer c
    ON f.CustomerKey = c.CustomerKey
GROUP BY c.CustomerName;


/* CTE */

WITH SalesCTE AS
(
    SELECT *
    FROM FactSales
)
SELECT *
FROM SalesCTE;


/* WINDOW FUNCTION */

SELECT
    CustomerKey,
    Amount,
    ROW_NUMBER() OVER
    (
        PARTITION BY CustomerKey
        ORDER BY Amount DESC
    ) AS RankNumber
FROM FactSales;