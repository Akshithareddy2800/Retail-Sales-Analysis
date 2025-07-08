-- Create the database
CREATE DATABASE IF NOT EXISTS retail_sales;
USE retail_sales;

-- Create customers table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    age INT,
    gender CHAR(1),
    city VARCHAR(50),
    state VARCHAR(2)
);

-- Create products table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    subcategory VARCHAR(50),
    price DECIMAL(10,2)
);

-- Create sales table
CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    date DATE,
    customer_id INT,
    product_id INT,
    quantity INT,
    unit_price DECIMAL(10,2),
    total_amount DECIMAL(10,2),
    store_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
); 