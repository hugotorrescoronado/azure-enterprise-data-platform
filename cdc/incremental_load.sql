DECLARE @LastLoadDate DATETIME;

SET @LastLoadDate =
(
    SELECT LastLoadDate
    FROM ETL_Control
    WHERE PipelineName='Customers'
);

SELECT *
FROM Customers
WHERE LastModified >
      @LastLoadDate;