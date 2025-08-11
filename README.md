## 🛠 Retail Sales Data Cleaning & Automation Pipeline



## 📌 Project Overview
This project automates the cleaning and transformation of messy, multi-source retail sales data using Python, Pandas, and NumPy.
It prepares raw data for dashboards, analytics, and machine learning by standardizing column names, handling missing values, converting data types, removing duplicates, and creating new calculated fields.

## 📂 Project Files
File	Description
cleaning_pipeline.py	Main automation script for cleaning the dataset.
cleaning_pipeline.ipynb	Development/testing notebook.
retail_store_sales.csv	Raw dataset (sample retail transaction data).
retail_store_sales_cleaned.csv	Cleaned dataset output.
Data Cleaning & Automation Documentation.pdf	Detailed documentation of the project.

## 📊 Dataset Overview
- Raw Data File: retail_store_sales.csv

- Output File: retail_store_sales_cleaned.csv

- Data Size: ~1,000–10,000 rows (sample)

- Industry Use Case: Retail / E-commerce

## Column Name	Description
 transaction_date |	Date of purchase |
| quantity |	Number of items bought |
| price_per_unit |	Price of each item |
| category |	Product category | 
| location |	Store or delivery location |
| payment_method |	Payment type (Cash, Card, UPI, etc.) |

## ⚙️ Tech Stack
- Language: Python

- Libraries: Pandas, NumPy

- Tools: Jupyter Notebook, CLI Execution

## 🔄 Data Cleaning Workflow
The cleaning logic is implemented in:

def clean_retail_data(input_file, output_file):
    ...
    
# Steps Performed:
✔ Column Standardization – Lowercase, underscores, strip spaces
✔ Date Conversion – Convert to datetime format
✔ Numeric Conversion – Median imputation for invalid quantity & price_per_unit
✔ Feature Engineering – total_spent = quantity × price_per_unit
✔ Text Cleaning – Standardized formatting for text fields
✔ Missing Value Handling – Fill with "Unknown" or median
✔ Duplicate Removal – Drop exact duplicates
✔ Output Generation – Save cleaned dataset as CSV

## 🚀 How to Run
# 1️⃣ Clone the Repository
git clone https://github.com/yourusername/retail-data-cleaning-pipeline.git
cd retail-data-cleaning-pipeline

# 2️⃣ Run the Script
python cleaning_pipeline.py

# 3️⃣ Output
Input: retail_store_sales.csv
Output: retail_store_sales_cleaned.csv

## 💼 Use Cases
- Retail / E-commerce reporting & analytics

- Automated pre-processing before creating dashboards in Tableau or Power BI

- Data preparation for machine learning models

- Standardizing multi-source transactional data

## 🏆 Skills Demonstrated
- Automated Data Cleaning

- Handling Missing & Corrupt Data

- Data Type Standardization

- Feature Engineering

- Reusable Pipeline Development

## 📬 Contact
Vaishnavi Ganeshkar
📧 vaishnaviganeshkar15@gmail.com
🔗 LinkedIn

💡 If you like this project, don’t forget to ⭐ star the repo!
