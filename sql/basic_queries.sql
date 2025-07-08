-- 1. View all customers
SELECT * FROM customers;

-- 2. View all products
SELECT * FROM products;

-- 3. View all sales
SELECT * FROM sales;

-- 4. Find total sales amount
SELECT SUM(total_amount) as total_sales
FROM sales;

-- 5. Find sales by date
SELECT date, SUM(total_amount) as daily_sales
FROM sales
GROUP BY date
ORDER BY date;

-- 6. Find top selling products
SELECT 
    p.product_name,
    SUM(s.quantity) as total_quantity_sold,
    SUM(s.total_amount) as total_revenue
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_quantity_sold DESC;

-- 7. Find customer purchase history
SELECT 
    c.customer_name,
    p.product_name,
    s.quantity,
    s.total_amount,
    s.date
FROM sales s
JOIN customers c ON s.customer_id = c.customer_id
JOIN products p ON s.product_id = p.product_id
ORDER BY c.customer_name, s.date;

-- 8. Find sales by category
SELECT 
    p.category,
    COUNT(*) as number_of_sales,
    SUM(s.total_amount) as total_revenue
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY p.category
ORDER BY total_revenue DESC; 