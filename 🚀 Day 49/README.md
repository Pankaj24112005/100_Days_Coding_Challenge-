# 🚀 Day 49 – SQL: LIMIT, DISTINCT, ALIAS

Welcome to Day 49 of my 100 Days Coding Challenge!

---

## 📌 Topics Covered

### ✅ LIMIT
Restricts number of rows.

SELECT * FROM students LIMIT 5;

---

### ✅ DISTINCT
Returns unique values.

SELECT DISTINCT city FROM students;

---

### ✅ ALIAS
Temporary rename.

SELECT name AS Student_Name FROM students;
SELECT s.age FROM students AS s;

---

## 🧠 Why These Matter

LIMIT → Preview data  
DISTINCT → Find unique records  
ALIAS → Clean readable queries  

Used heavily in analytics & backend systems.

---

## 🛠 Sample Table

CREATE TABLE students (
id INT,
name VARCHAR(50),
age INT,
city VARCHAR(50)
);

INSERT INTO students VALUES
(1,'Pankaj',21,'Pune'),
(2,'Amit',22,'Mumbai'),
(3,'Riya',20,'Pune'),
(4,'Sneha',23,'Delhi'),
(5,'Rahul',21,'Mumbai');

---

## 🎯 Practice Queries

SELECT * FROM students LIMIT 3;

SELECT DISTINCT city FROM students;

SELECT name AS StudentName FROM students;

SELECT s.age FROM students AS s;

---

## 🔗 GitHub Folder

https://github.com/Pankaj24112005/100_Days_Coding_Challenge-/tree/main/%F0%9F%9A%80%20Day%2049

---

🔥 Learning one day at a time.

#SQL #100DaysOfCode #Day49 #AIandDataScience
