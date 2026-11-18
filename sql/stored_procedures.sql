CREATE PROCEDURE sp_LoadCustomers
AS
BEGIN

INSERT INTO DimCustomer
(
 CustomerKey,
 CustomerName,
 City
)
SELECT
 customer_id,
 customer_name,
 city
FROM staging_customers;

END