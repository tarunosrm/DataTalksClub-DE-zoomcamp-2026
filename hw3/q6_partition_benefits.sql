--will process 310.24 MB bytes processed
--query non-partitioned table
SELECT DISTINCT VendorID
FROM `taxi-rides-ny-bq.dezoomcamp_hw3_bq.yellow_tripdata_2024`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15';

--query partitioned table 
--26.84 bytes processed
SELECT DISTINCT VendorID
FROM `taxi-rides-ny-bq.dezoomcamp_hw3_bq.yellow_tripdata_2024_optimized`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15';

--310.24 MB for non-partitioned table and 26.84 MB for the partitioned table
