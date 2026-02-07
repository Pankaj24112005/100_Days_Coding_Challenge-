-- 🚀 Day 50 – SQL Aggregate Functions Practice

SHOW DATABASES;
use student_db;

-- Create table
CREATE TABLE students1 (
    id INT,
    name VARCHAR(50),
    age INT,
    marks INT
);

-- Insert sample data
INSERT INTO students1 VALUES
(1, 'Rahul', 20, 75),
(2, 'Sneha', 21, 88),
(3, 'Amit', 20, 65),
(4, 'Pooja', 22, 90),
(5, 'Ravi', 21, 55),
(6, 'Neha', 22, 72);


SELECT * FROM students1;
---------------------------------------------------

-- 1. Count total students
SELECT COUNT(*) AS total_students FROM students;

-- 2. Find sum of marks
SELECT SUM(marks) AS total_marks FROM students;

-- 3. Find average marks
SELECT AVG(marks) AS average_marks FROM students;

-- 4. Find maximum marks
SELECT MAX(marks) AS highest_marks FROM students;

-- 5. Find minimum marks
SELECT MIN(marks) AS lowest_marks FROM students;

---------------------------------------------------

-- 6. Count students age-wise
SELECT age, COUNT(*) AS student_count
FROM students
GROUP BY age;

-- 7. Average marks by age
SELECT age, AVG(marks) AS avg_marks
FROM students
GROUP BY age;

---------------------------------------------------

-- 8. Total marks by age
SELECT age, SUM(marks) AS total_marks
FROM students
GROUP BY age;

-- 9. Count students with marks above 70
SELECT COUNT(*) FROM students
WHERE marks > 70;

-- 10. Average marks where age is greater than 20
SELECT AVG(marks)
FROM students
WHERE age > 20;

---------------------------------------------------

-- 11. Highest marks age-wise
SELECT age, MAX(marks)
FROM students
GROUP BY age;

-- 12. Lowest marks age-wise
SELECT age, MIN(marks)
FROM students
GROUP BY age;

---------------------------------------------------

-- End of Day 50 Practice
