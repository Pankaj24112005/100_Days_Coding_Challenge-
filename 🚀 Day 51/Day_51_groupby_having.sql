-- 🚀 Day 51 – GROUP BY & HAVING Practice File
-- Part of 100 Days Coding Challenge

-- =========================
-- Create Database
-- =========================
CREATE DATABASE IF NOT EXISTS day51_sql;
USE day51_sql;

-- =========================
-- Employees Table
-- =========================
CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    department VARCHAR(50),
    salary INT
);

INSERT INTO employees (name, department, salary) VALUES
('Rahul','IT',50000),
('Anita','HR',40000),
('Amit','IT',60000),
('Sneha','Finance',45000),
('Rohit','HR',42000),
('Priya','IT',55000);

-- =========================
-- Customers Table
-- =========================
CREATE TABLE customers (
    cust_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    city VARCHAR(50)
);

INSERT INTO customers (name, city) VALUES
('Pankaj','Pune'),
('Ravi','Mumbai'),
('Neha','Pune'),
('Kiran','Delhi'),
('Asha','Pune'),
('Vikas','Mumbai');

-- =========================
-- Students Table
-- =========================
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    subject VARCHAR(50),
    marks INT
);

INSERT INTO students (name, subject, marks) VALUES
('Arjun','Math',85),
('Meera','Math',75),
('Riya','Science',90),
('Kabir','Science',70),
('Anmol','English',88);

-- =========================
-- Orders Table
-- =========================
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    category VARCHAR(50),
    sales INT
);

INSERT INTO orders (category, sales) VALUES
('Electronics',3000),
('Electronics',2500),
('Clothing',1500),
('Clothing',2000),
('Grocery',4000);

-- =========================
-- PRACTICE QUERIES
-- =========================

-- 1. Count employees per department
SELECT department, COUNT(*) AS total_employees
FROM employees
GROUP BY department;

-- 2. Total salary by department
SELECT department, SUM(salary) AS total_salary
FROM employees
GROUP BY department;

-- 3. Departments having more than 2 employees
SELECT department, COUNT(*) AS emp_count
FROM employees
GROUP BY department
HAVING COUNT(*) > 2;

-- 4. Customers count by city
SELECT city, COUNT(*) AS total_customers
FROM customers
GROUP BY city;

-- 5. Cities having more than 2 customers
SELECT city, COUNT(*)
FROM customers
GROUP BY city
HAVING COUNT(*) > 2;

-- 6. Average marks per subject
SELECT subject, AVG(marks) AS avg_marks
FROM students
GROUP BY subject;

-- 7. Categories with total sales above 4000
SELECT category, SUM(sales) AS total_sales
FROM orders
GROUP BY category
HAVING SUM(sales) > 4000;

-- =========================
-- END OF DAY 51
-- =========================
