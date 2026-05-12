-- 🚀 Day 52 – SQL JOINS Practice File
-- INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN

-- Create Database
CREATE DATABASE IF NOT EXISTS day52_sql;
USE day52_sql;

-- =========================
-- Create Tables
-- =========================

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product VARCHAR(50),
    amount INT
);

-- =========================
-- Insert Sample Data
-- =========================

INSERT INTO customers VALUES
(1, 'Pankaj'),
(2, 'Rahul'),
(3, 'Sneha'),
(4, 'Amit');

INSERT INTO orders VALUES
(101, 1, 'Laptop', 60000),
(102, 2, 'Mobile', 20000),
(103, 1, 'Mouse', 1000),
(104, 5, 'Keyboard', 1500);

-- =========================
-- INNER JOIN
-- =========================

SELECT customers.customer_name, orders.product, orders.amount
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id;

-- =========================
-- LEFT JOIN
-- =========================

SELECT customers.customer_name, orders.product
FROM customers
LEFT JOIN orders
ON customers.customer_id = orders.customer_id;

-- =========================
-- RIGHT JOIN
-- =========================

SELECT customers.customer_name, orders.product
FROM customers
RIGHT JOIN orders
ON customers.customer_id = orders.customer_id;

-- =========================
-- FULL JOIN (MySQL workaround)
-- =========================

SELECT customers.customer_name, orders.product
FROM customers
LEFT JOIN orders
ON customers.customer_id = orders.customer_id

UNION

SELECT customers.customer_name, orders.product
FROM customers
RIGHT JOIN orders
ON customers.customer_id = orders.customer_id;

-- =========================
-- BONUS PRACTICE QUERIES
-- =========================

-- Customers who never ordered
SELECT customers.customer_name
FROM customers
LEFT JOIN orders
ON customers.customer_id = orders.customer_id
WHERE orders.customer_id IS NULL;

-- Total amount spent by each customer
SELECT customers.customer_name, SUM(orders.amount) AS total_spent
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_name;

-- Orders without matching customers
SELECT orders.product
FROM orders
LEFT JOIN customers
ON orders.customer_id = customers.customer_id
WHERE customers.customer_id IS NULL;
