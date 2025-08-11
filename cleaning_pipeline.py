import pandas as pd
import numpy as np

def clean_retail_data(input_file, output_file):
    df = pd.read_csv(input_file)

    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce')
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce').fillna(df['quantity'].median())
    df['price_per_unit'] = pd.to_numeric(df['price_per_unit'], errors='coerce').fillna(df['price_per_unit'].median())
    df['total_spent'] = df['quantity'] * df['price_per_unit']
    df['category'] = df['category'].fillna('Unknown').str.strip().str.title()
    df['location'] = df['location'].fillna('Unknown').str.strip().str.title()
    df['payment_method'] = df['payment_method'].fillna('Unknown').str.strip().str.title()
    df = df.drop_duplicates()

    df.to_csv(output_file, index=False)
    print(f'Data cleaned & saved to {output_file}')

# Run the pipeline
if __name__ == "__main__":
    clean_retail_data('retail_store_sales.csv', 'retail_store_sales_cleaned.csv')
