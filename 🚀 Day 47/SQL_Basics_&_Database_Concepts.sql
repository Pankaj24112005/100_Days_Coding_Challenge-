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

SHOW TABLES;

DESCRIBE students;

select * from students;


