
--Counting zero fare trips
SELECT COUNT(*) as zero_fare_count
FROM `taxi-rides-ny-bq.dezoomcamp_hw3_bq.yellow_tripdata_2024`
WHERE fare_amount = 0;

--why 0 fare trips
SELECT 
  COUNT(*) as zero_fare_count,
  AVG(trip_distance) as avg_distance,
  MIN(tpep_pickup_datetime) as earliest_trip,
  MAX(tpep_pickup_datetime) as latest_trip
FROM `taxi-rides-ny-bq.dezoomcamp_hw3_bq.yellow_tripdata_2024`
WHERE fare_amount = 0;
/*


8,333 trips had a fare of $0
Average distance: ~3.23 miles (not short trips!)
Date range: Spans the entire 6-month period (January - June 2024)

Why Zero Fares?
These could be:

Cancelled trips after pickup
Driver adjustments or refunds
Voided transactions
Data errors
Dispute resolution credits

The fact that the average distance is 3.2 miles suggests many of these were actual trips, not just immediate cancellations!*/
