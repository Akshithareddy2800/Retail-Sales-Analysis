"""
This script generates visualizations from processed sales data.

Mermaid Diagram (Visualization Workflow):

    ```mermaid
    graph TD;
        A[Processed Data] --> B[create_visualizations.py]
        B --> C[Charts & Graphs]
    ```
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',  # Add your MySQL password here
            database='retail_sales'
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def get_sales_data():
    connection = create_connection()
    if connection is None:
        return None
    
    try:
        # Query to get sales data with product and customer information
        query = """
        SELECT 
            s.date,
            s.total_amount,
            p.product_name,
            p.category,
            c.customer_name,
            c.city,
            c.state
        FROM sales s
        JOIN products p ON s.product_id = p.product_id
        JOIN customers c ON s.customer_id = c.customer_id
        """
        
        df = pd.read_sql(query, connection)
        return df
    except Error as e:
        print(f"Error fetching data: {e}")
        return None
    finally:
        connection.close()

def create_visualizations():
    # Set style
    plt.style.use('seaborn')
    sns.set_palette("husl")
    
    # Get data
    df = get_sales_data()
    if df is None:
        return
    
    # 1. Daily Sales Trend
    plt.figure(figsize=(12, 6))
    daily_sales = df.groupby('date')['total_amount'].sum()
    daily_sales.plot(kind='line', marker='o')
    plt.title('Daily Sales Trend')
    plt.xlabel('Date')
    plt.ylabel('Total Sales Amount ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('visualizations/daily_sales_trend.png')
    plt.close()
    
    # 2. Sales by Category
    plt.figure(figsize=(10, 6))
    category_sales = df.groupby('category')['total_amount'].sum()
    category_sales.plot(kind='bar')
    plt.title('Sales by Category')
    plt.xlabel('Category')
    plt.ylabel('Total Sales Amount ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('visualizations/sales_by_category.png')
    plt.close()
    
    # 3. Product Performance
    plt.figure(figsize=(12, 6))
    product_sales = df.groupby('product_name')['total_amount'].sum().sort_values(ascending=False)
    product_sales.plot(kind='bar')
    plt.title('Product Performance by Sales')
    plt.xlabel('Product')
    plt.ylabel('Total Sales Amount ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('visualizations/product_performance.png')
    plt.close()
    
    # 4. Sales Distribution by State
    plt.figure(figsize=(10, 6))
    state_sales = df.groupby('state')['total_amount'].sum()
    state_sales.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Sales Distribution by State')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig('visualizations/sales_by_state.png')
    plt.close()
    
    # 5. Customer Age Distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='age', bins=5)
    plt.title('Customer Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig('visualizations/customer_age_distribution.png')
    plt.close()

if __name__ == "__main__":
    create_visualizations()
    print("Visualizations have been created in the 'visualizations' directory!") 