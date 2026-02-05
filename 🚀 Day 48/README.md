===
   Day 48 – SQL : SELECT, WHERE, ORDER BY
   100 Days Coding Challenge
=== 

 Table Structure ==
CREATE TABLE students (
    id INT,
    name VARCHAR(50),
    age INT,
    city VARCHAR(50)
);

Sample Data
INSERT INTO students VALUES (1, 'Rahul', 21, 'Mumbai');
INSERT INTO students VALUES (2, 'Sneha', 22, 'Pune');
INSERT INTO students VALUES (3, 'Amit', 20, 'Delhi');
INSERT INTO students VALUES (4, 'Riya', 23, 'Delhi');
INSERT INTO students VALUES (5, 'Karan', 19, 'Mumbai');

=====================
   SELECT
===================== 

SELECT * FROM students;
SELECT name, city FROM students;

=====================
   WHERE
===================== 

SELECT * FROM students WHERE age > 20;
SELECT * FROM students WHERE city = 'Delhi';
SELECT * FROM students WHERE name LIKE 'A%';
SELECT * FROM students WHERE age BETWEEN 18 AND 25;
SELECT * FROM students WHERE city IN ('Delhi','Mumbai');

=====================
   ORDER BY
===================== 

SELECT * FROM students ORDER BY age ASC;
SELECT * FROM students ORDER BY age DESC;

=====================
   COMBINED QUERIES
===================== 

SELECT * FROM students
WHERE city='Delhi'
ORDER BY age DESC;

SELECT name, age FROM students
WHERE age > 20
ORDER BY age ASC;

=====================
   MINI PRACTICE
===================== 

-- Students older than 21
SELECT * FROM students WHERE age > 21;

-- Sort by name
SELECT * FROM students ORDER BY name;

-- Only Delhi students
SELECT * FROM students WHERE city='Delhi';

-- Show name + age
SELECT name, age FROM students;

-- Names ending with 't'
SELECT * FROM students WHERE name LIKE '%t';

=========================================
   Day 48 Completed 🚀
========================================= */
