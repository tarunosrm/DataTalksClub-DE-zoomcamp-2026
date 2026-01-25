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

## 🌍 Terraform Homework – Environment Setup

In this section of the homework, we prepare the environment by creating resources in **Google Cloud Platform (GCP)** using **Terraform**.

---

### 📂 Files
- `main.tf` → Defines the provider (`hashicorp/google`), a GCS bucket, and a BigQuery dataset.
- `variables.tf` → Stores project ID, region, location, bucket name, dataset name, and credentials path.
- `outputs.tf` → Prints the bucket name and dataset ID after apply.

---

### 🛠 Resources Created
1. **Google Cloud Storage Bucket**
   - Name: `terraform-test-485109-terra-bucket`
   - Location: `US`
   - Storage Class: `STANDARD`
   - Lifecycle Rule: Delete objects older than 1 day
   - Force destroy enabled

2. **BigQuery Dataset**
   - Dataset ID: `demo_dataset_bq`
   - Location: `US`
   - Delete contents on destroy enabled

---

### ▶️ Terraform Workflow
Run the following commands inside the `terrademo` directory:

```bash
terraform init -upgrade   # Initialize and fetch provider plugins
terraform plan            # Preview resources to be created
terraform apply -auto-approve   # Create bucket + dataset
terraform destroy -auto-approve #destroy bucket and bigQuery dataset


