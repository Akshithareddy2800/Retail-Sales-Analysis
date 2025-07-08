"""
This script imports raw CSV data into the SQL database for analysis.

Mermaid Diagram (Data Import Flow):

    ```mermaid
    graph TD;
        A[Raw CSV Files] --> B[import_data.py]
        B --> C[SQL Database]
    ```
"""
import pandas as pd
import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Ak@1mysqlroot',  # Replace this with your actual MySQL password
            database='retail_sales'
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def import_data():
    # Read CSV files
    customers_df = pd.read_csv('data/raw/customers.csv')
    products_df = pd.read_csv('data/raw/products.csv')
    sales_df = pd.read_csv('data/raw/sales.csv')
    
    # Convert date column to proper format
    sales_df['date'] = pd.to_datetime(sales_df['date']).dt.strftime('%Y-%m-%d')
    
    connection = create_connection()
    if connection is None:
        return
    
    cursor = connection.cursor()
    
    try:
        # Import customers
        for _, row in customers_df.iterrows():
            sql = """INSERT INTO customers 
                    (customer_id, customer_name, age, gender, city, state) 
                    VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, tuple(row))
        
        # Import products
        for _, row in products_df.iterrows():
            sql = """INSERT INTO products 
                    (product_id, product_name, category, subcategory, price) 
                    VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(sql, tuple(row))
        
        # Import sales
        for _, row in sales_df.iterrows():
            sql = """INSERT INTO sales 
                    (sale_id, date, customer_id, product_id, quantity, 
                     unit_price, total_amount, store_id) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, tuple(row))
        
        connection.commit()
        print("Data imported successfully!")
        
    except Error as e:
        print(f"Error importing data: {e}")
        connection.rollback()
    
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    import_data() 