CREATE DATABASE student_db;

use student_db;
-- Day 49
-- students(id, name, age, city)

-- LIMIT QUERIES
-- Get first 5 students
SELECT * FROM students LIMIT 5;

-- Get first 3 names only
SELECT name FROM students LIMIT 3;

-- Skip first 2 rows and get next 3 (pagination)
SELECT * FROM students LIMIT 3 OFFSET 2;

-- Youngest 3 students
SELECT * FROM students
ORDER BY age ASC
LIMIT 3;

-- DISTINCT QUERIES
-- Unique cities
SELECT DISTINCT city FROM students;

-- Unique ages
SELECT DISTINCT age FROM students;

-- Count unique cities
SELECT COUNT(DISTINCT city) FROM students;

-- Unique city + age pairs
SELECT DISTINCT city, age FROM students;


-- ALIAS QUERIES

-- Rename column
SELECT name AS Student_Name FROM students;

-- Rename multiple columns
SELECT id AS RollNo, age AS StudentAge FROM students;

-- Table alias
SELECT s.name FROM students AS s;

-- Alias with calculation
SELECT name, age+1 AS NextYearAge FROM students;

-- COMBINED (LIMIT + DISTINCT + ALIAS)
-- First 2 unique cities
SELECT DISTINCT city AS CityName
FROM students
LIMIT 2;

-- Top 3 oldest students
SELECT name AS StudentName, age
FROM students
ORDER BY age DESC
LIMIT 3;

-- Unique cities with alias
SELECT DISTINCT city AS Location
FROM students;





