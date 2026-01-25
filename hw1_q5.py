import pandas as pd

# Step 1: Load datasets
df = pd.read_parquet("green_tripdata_2025-11.parquet")
zones = pd.read_csv("taxi_zone_lookup.csv")

# Step 2: Filter by date
df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])
df_nov18 = df[df['lpep_pickup_datetime'].dt.date == pd.to_datetime("2025-11-18").date()]

# Step 3: Join with zone lookup
df_nov18 = df_nov18.merge(zones, left_on="PULocationID", right_on="LocationID")

# Step 4: Restrict to given zones
target_zones = ["East Harlem North", "East Harlem South", "Morningside Heights", "Forest Hills"]
df_nov18 = df_nov18[df_nov18['Zone'].isin(target_zones)]

# Step 5: Group by zone and sum total_amount
zone_totals = df_nov18.groupby('Zone')['total_amount'].sum()

# Step 6: Find biggest pickup zone
biggest_zone = zone_totals.idxmax()
largest_total = zone_totals.max()

print("Pickup zone with largest total_amount:", biggest_zone)
print("Total amount:", largest_total)

# Optional: print all zones ranked
print(zone_totals.sort_values(ascending=False))
