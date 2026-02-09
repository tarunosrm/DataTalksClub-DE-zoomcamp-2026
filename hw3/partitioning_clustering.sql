--Create partitioned and clustered (optimized) table
CREATE OR REPLACE TABLE `taxi-rides-ny-bq.dezoomcamp_hw3_bq.yellow_tripdata_2024_optimized`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID
AS
SELECT *
FROM `taxi-rides-ny-bq.dezoomcamp_hw3_bq.yellow_tripdata_2024`;

--Test optimization

---unoptimized table
SELECT VendorID, COUNT(*) as trip_count
FROM `taxi-rides-ny-bq.dezoomcamp_hw3.yellow_tripdata_2024`
WHERE tpep_dropoff_datetime BETWEEN '2024-01-01' AND '2024-01-31'
ORDER BY VendorID;
---optimized table

SELECT VendorID, COUNT(*) as trip_count
FROM `taxi-rides-ny-bq.dezoomcamp_hw3.yellow_tripdata_2024_optimized`
WHERE tpep_dropoff_datetime BETWEEN '2024-01-01' AND '2024-01-31'
ORDER BY VendorID;
