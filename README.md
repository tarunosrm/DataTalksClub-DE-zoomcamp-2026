# Homework Scripts – Week 1 (Docker & Terraform)

This section documents the Python scripts for Homework Questions 3 to 6 from the **DataTalksClub DE Zoomcamp 2026**.

---

## 📂 Scripts Overview

### `hw1_q3.py`
**Task:**  
Filter NYC Green Taxi trip data for **November 18, 2025**, join with zone lookup, restrict to specific zones, and compute the **pickup zone with the largest total amount**.  

**Key steps:**  
- Load `green_tripdata_2025-11.parquet` and `taxi_zone_lookup.csv`  
- Filter trips by date (`2025-11-18`)  
- Merge with zone lookup for pickup zones  
- Restrict to target zones (East Harlem North/South, Morningside Heights, Forest Hills)  
- Group by zone and sum `total_amount`  
- Identify the zone with the largest total  

---

### `hw1_q4.py`
**Task:**  
Compute the **average trip distance** for passengers picked up in **East Harlem North** in November 2025.  

**Key steps:**  
- Filter trips by pickup zone = “East Harlem North”  
- Calculate mean of `trip_distance`  
- Print result  

---

### `hw1_q5.py`
**Task:**  
Find the **drop-off zone with the largest total amount** for passengers picked up in **East Harlem North** in November 2025.  

**Key steps:**  
- Merge trip data with zone lookup for both pickup and drop-off zones  
- Filter pickups in “East Harlem North”  
- Group by drop-off zone and sum `total_amount`  
- Identify the drop-off zone with the largest total  

---

### `hw1_q6.py`
**Task:**  
Find the **drop-off zone with the largest tip amount** for passengers picked up in **East Harlem North** in November 2025.  

**Key steps:**  
- Merge trip data with zone lookup for both pickup and drop-off zones  
- Filter pickups in “East Harlem North”  
- Group by drop-off zone and sum `tip_amount`  
- Identify the drop-off zone with the largest tip  

---

## 🛠 How to Run
Each script can be executed directly from the command line inside your container:

```bash
python hw1_q3.py
python hw1_q4.py
python hw1_q5.py
python hw1_q6.py
