/* =========================================
   Day 55 – SQL Case Study
   Topic: SQL Case Study Practice
========================================= */

-- Create Database
CREATE DATABASE IF NOT EXISTS day55_case_study;
USE day55_case_study;

-- =========================
-- Table Creation
-- =========================

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    department VARCHAR(30),
    salary INT,
    joining_date DATE
);

-- =========================
-- Insert Sample Data
-- =========================

INSERT INTO employees VALUES
(1,'Amit','IT',60000,'2022-01-10'),
(2,'Neha','HR',45000,'2021-05-15'),
(3,'Rahul','IT',75000,'2020-03-20'),
(4,'Priya','Finance',50000,'2022-07-01'),
(5,'Rohit','IT',55000,'2021-09-12'),
(6,'Sneha','HR',48000,'2020-11-25'),
(7,'Arjun','Finance',65000,'2019-06-18'),
(8,'Kiran','IT',80000,'2018-02-10');

-- =========================
-- CASE STUDY QUESTIONS
-- =========================

-- Q1: Find highest salary employee from each department
SELECT department, emp_name, salary
FROM employees e
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
    WHERE department = e.department
);

-- -------------------------

-- Q2: Rank employees based on salary (overall)

SELECT emp_name, salary,
RANK() OVER(ORDER BY salary DESC) AS salary_rank
FROM employees;

-- -------------------------

-- Q3: Find employees earning above department average

SELECT emp_name, department, salary
FROM employees e
WHERE salary >
(
    SELECT AVG(salary)
    FROM employees
    WHERE department = e.department
);

-- -------------------------

-- Q4: Second highest salary (Interview Classic)

SELECT MAX(salary) AS second_highest_salary
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

-- -------------------------

-- Q5: Total salary per department (only >100000)

SELECT department, SUM(salary) AS total_salary
FROM employees
GROUP BY department
HAVING SUM(salary) > 100000;

-- -------------------------

-- Q6: Using CTE – Top 2 salaries

WITH ranked_emp AS (
    SELECT emp_name, salary,
    DENSE_RANK() OVER(ORDER BY salary DESC) AS rnk
    FROM employees
)
SELECT emp_name, salary
FROM ranked_emp
WHERE rnk <= 2;

-- -------------------------

-- Q7: Count employees per department

SELECT department, COUNT(*) AS emp_count
FROM employees
GROUP BY department;

-- -------------------------

-- Q8: Oldest employee (by joining date)

SELECT *
FROM employees
ORDER BY joining_date ASC
LIMIT 1;

-- -------------------------

-- Q9: IT department employees sorted by salary

SELECT *
FROM employees
WHERE department = 'IT'
ORDER BY salary DESC;

-- -------------------------

-- Q10: Salary Category using CASE

SELECT emp_name, salary,
CASE
    WHEN salary >= 70000 THEN 'High'
    WHEN salary BETWEEN 50000 AND 69999 THEN 'Medium'
    ELSE 'Low'
END AS salary_level
FROM employees;

-- =========================
-- END OF FILE
-- =========================
