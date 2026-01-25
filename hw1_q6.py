import pandas as pd

# Step 1: Load datasets
df = pd.read_parquet("green_tripdata_2025-11.parquet")
zones = pd.read_csv("taxi_zone_lookup.csv")

# Step 2: Convert pickup/dropoff times to datetime
df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])

# Step 3: Filter for November 2025
df_nov = df[df['lpep_pickup_datetime'].dt.month == 11]
df_nov = df_nov[df_nov['lpep_pickup_datetime'].dt.year == 2025]

# Step 4: Merge with zone lookup for pickup and dropoff
df_nov = df_nov.merge(zones, left_on="PULocationID", right_on="LocationID", suffixes=("", "_PU"))
df_nov = df_nov.merge(zones, left_on="DOLocationID", right_on="LocationID", suffixes=("", "_DO"))

# Step 5: Restrict to pickups in East Harlem North
df_ehn = df_nov[df_nov['Zone'] == "East Harlem North"]

# Step 6: Group by dropoff zone and find largest tip
dropoff_tips = df_ehn.groupby('Zone_DO')['tip_amount'].sum()
largest_dropoff_zone = dropoff_tips.idxmax()
largest_tip = dropoff_tips.max()

print("Dropoff zone with largest tip:", largest_dropoff_zone)
print("Total tip amount:", largest_tip)
print(dropoff_tips.sort_values(ascending=False))
