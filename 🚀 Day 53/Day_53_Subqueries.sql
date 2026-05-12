-- ==========================================
-- Day 53 - SQL Subqueries
-- 100 Days Coding Challenge
-- ==========================================
SHOW DATABASES;
CREATE DATABASE Day_53; 
USE Day_53;
-- Create table
CREATE TABLE employee (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept VARCHAR(50),
    salary INT
);

-- Insert sample records
INSERT INTO employee VALUES
(1, 'Ankit', 'IT', 60000),
(2, 'Neha', 'HR', 45000),
(3, 'Rohit', 'IT', 70000),
(4, 'Pooja', 'Finance', 50000),
(5, 'Aman', 'HR', 55000);

-- ==========================================
-- 1. Single Row Subquery
-- Find employee with maximum salary
-- ==========================================

SELECT *
FROM employee
WHERE salary = (
    SELECT MAX(salary)
    FROM employee
);

-- ==========================================
-- 2. Subquery with IN
-- Find employees working in departments
-- having average salary > 50000
-- ==========================================

SELECT *
FROM employee
WHERE dept IN (
    SELECT dept
    FROM employee
    GROUP BY dept
    HAVING AVG(salary) > 50000
);

-- ==========================================
-- 3. Subquery with ANY
-- Find employees earning more than
-- ANY salary of HR department
-- ==========================================

SELECT *
FROM employee
WHERE salary > ANY (
    SELECT salary
    FROM employee
    WHERE dept = 'HR'
);

-- ==========================================
-- 4. Subquery with ALL
-- Find employees earning more than
-- ALL salaries of HR department
-- ==========================================

SELECT *
FROM employee
WHERE salary > ALL (
    SELECT salary
    FROM employee
    WHERE dept = 'HR'
);

-- ==========================================
-- 5. Subquery in SELECT clause
-- ==========================================

SELECT emp_name,
       salary,
       (SELECT AVG(salary) FROM employee) AS avg_salary
FROM employee;

-- ==========================================
-- 6. Subquery in FROM clause
-- ==========================================

SELECT d.dept, d.avg_salary
FROM (
    SELECT dept, AVG(salary) AS avg_salary
    FROM employee
    GROUP BY dept
) d;

-- ==========================================
-- 7. Correlated Subquery
-- Find employees earning more than
-- their department average
-- ==========================================

SELECT *
FROM employee e1
WHERE salary > (
    SELECT AVG(salary)
    FROM employee e2
    WHERE e1.dept = e2.dept
);

-- ==========================================
-- End of Day 53 - Subqueries
-- ==========================================
