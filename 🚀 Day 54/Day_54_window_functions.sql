-- 🚀 Day 54 – SQL Window Functions Practice
-- ===============================
-- Create New Database
-- ===============================

CREATE DATABASE day54_window_functions;
USE day54_window_functions;

-- ===============================
-- Create Sample Table
-- ===============================

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    department VARCHAR(50),
    salary INT
);

-- ===============================
-- Insert Sample Data
-- ===============================

INSERT INTO employees VALUES
(1,'Amit','IT',60000),
(2,'Neha','IT',75000),
(3,'Raj','HR',50000),
(4,'Priya','HR',65000),
(5,'Kunal','Finance',70000),
(6,'Sneha','Finance',72000),
(7,'Ravi','IT',80000),
(8,'Pooja','HR',55000);

-- ===============================
-- View Table
-- ===============================

SELECT * FROM employees;

-- ===============================
-- ROW_NUMBER()
-- ===============================

SELECT *,
ROW_NUMBER() OVER(ORDER BY salary DESC) AS row_num
FROM employees;

-- ===============================
-- RANK()
-- ===============================

SELECT *,
RANK() OVER(ORDER BY salary DESC) AS salary_rank
FROM employees;

-- ===============================
-- DENSE_RANK()
-- ===============================

SELECT *
DENSE_RANK() OVER(ORDER BY salary DESC) AS dense_rank
FROM employees;

-- ===============================
-- PARTITION BY (Department Ranking)
-- ===============================

SELECT *,
ROW_NUMBER() OVER(PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;

-- ===============================
-- LAG()
-- ===============================

SELECT emp_name, salary,
LAG(salary) OVER(ORDER BY salary) AS prev_salary
FROM employees;

-- ===============================
-- LEAD()
-- ===============================

SELECT emp_name, salary,
LEAD(salary) OVER(ORDER BY salary) AS next_salary
FROM employees;

-- ===============================
-- Salary Difference
-- ===============================

SELECT emp_name, salary,
salary - LAG(salary) OVER(ORDER BY salary) AS salary_diff
FROM employees;

-- ===============================
-- Running Total
-- ===============================

SELECT emp_name, salary,
SUM(salary) OVER(ORDER BY salary) AS running_total
FROM employees;

-- ===============================
-- Department Wise Total Salary
-- ===============================

SELECT emp_name, department, salary,
SUM(salary) OVER(PARTITION BY department) AS dept_total_salary
FROM employees;

-- ===============================
-- Highest Paid Employee Per Department
-- ===============================

SELECT *
FROM (
    SELECT *,
    RANK() OVER(PARTITION BY department ORDER BY salary DESC) AS rnk
    FROM employees
) t
WHERE rnk = 1;

-- ===============================
-- END
-- ===============================
