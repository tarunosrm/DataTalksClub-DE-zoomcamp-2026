
import pandas as pd

# Load your parquet file
df = pd.read_parquet("green_tripdata_2025-11.parquet")

# Step 1: Filter trips less than 100 miles
df = df[df['trip_distance'] < 100]

# Step 2: Ensure pickup time is datetime
df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])

# Step 3: Extract pickup day
df['pickup_day'] = df['lpep_pickup_datetime'].dt.date

# Step 4: Find longest trip per day
longest_per_day = df.groupby('pickup_day')['trip_distance'].max()

# Step 5: Find the day with the longest trip overall
day_with_longest_trip = longest_per_day.idxmax()
longest_distance = longest_per_day.max()

print("Day with longest trip:", day_with_longest_trip)
print("Longest trip distance:", longest_distance)
print("record with longest trip:", df.loc[df['trip_distance'].idxmax()])

