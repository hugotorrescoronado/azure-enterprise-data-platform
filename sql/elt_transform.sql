INSERT INTO curated_customers

SELECT DISTINCT
       customer_id,
       UPPER(name),
       city
FROM raw_customers;