CREATE DATABASE student_db;

use student_db;

CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    city TEXT
);

INSERT INTO students VALUES (1, 'Rahul', 21, 'Pune');
INSERT INTO students VALUES (2, 'Priya', 22, 'Mumbai');
INSERT INTO students VALUES (3, 'Amit', 20, 'Delhi');

INSERT INTO students VALUES (4, 'sarang', 30, 'Hingoli');
INSERT INTO students VALUES (5, 'Prakruti', 22, 'Amravati');
INSERT INTO students VALUES (6, 'Soham', 18, 'Agra');

SHOW TABLES;

DESCRIBE students;

select * from students;


-- Fetch all records
SELECT * FROM students;

-- Fetch specific columns
SELECT name, city FROM students;

-- Filter students with age above 18
SELECT * FROM students WHERE age > 18;


-- Sort students by age
SELECT * FROM students ORDER BY age DESC;

-- Filter + sort together
SELECT * FROM students WHERE city='Mumbai' ORDER BY age ASC;






