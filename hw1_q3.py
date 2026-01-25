import pandas as pd

# Load the parquet file
df = pd.read_parquet("/data/green_tripdata_2025-11.parquet")

# Convert pickup datetime column to proper datetime type
df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])

# Filter for November 2025 trips
mask = (df['lpep_pickup_datetime'] >= "2025-11-01") & (df['lpep_pickup_datetime'] < "2025-12-01")

# Apply both filters: November trips AND distance <= 1 mile
short_trips = df.loc[mask & (df['trip_distance'] <= 1)]

# Count the number of trips
print("Number of short trips (<=1 mile):", len(short_trips))
