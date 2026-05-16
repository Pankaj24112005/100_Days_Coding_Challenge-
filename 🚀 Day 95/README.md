# 💾 SQL Interview Questions & Case Study Practice

## 🚀 Project Overview
This project contains important **SQL interview questions**, real-world **case study practice**, and business problem-solving queries frequently asked in Data Analyst and Data Science interviews.

The goal of this project is to strengthen:
- SQL fundamentals
- Query writing skills
- Business problem-solving
- Database analysis techniques
- Interview preparation

---

# 🛠️ Topics Covered

## 📌 SQL Fundamentals
- SELECT Statements
- WHERE Clause
- ORDER BY
- GROUP BY
- HAVING
- LIMIT

## 📌 Intermediate SQL
- JOINs
- Subqueries
- CASE Statements
- Aggregate Functions
- String Functions
- Date Functions

## 📌 Advanced SQL
- Window Functions
- CTEs (Common Table Expressions)
- Rank & Dense Rank
- Views
- Stored Procedures

---

# 📂 Project Structure

```bash
📁 SQL-Interview-Preparation
│
├── 📄 SQL_Interview_Questions.pdf
├── 📄 SQL_Case_Study.pdf
├── 📓 sql_practice_queries.sql
├── 📊 case_study_analysis.ipynb
├── 📈 sample_dataset.xlsx
├── 📑 SQL_Interview_Notes.pptx
└── 📄 README.md
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/sql-interview-preparation.git
```

## 2️⃣ Move into Project Directory

```bash
cd sql-interview-preparation
```

## 3️⃣ Install Required Libraries

```bash
pip install pandas numpy matplotlib
```

---

# ▶️ Run SQL Practice

Use:
- MySQL
- PostgreSQL
- SQLite
- SQL Server

Execute queries from:

```bash
sql_practice_queries.sql
```

---

# 🧠 Important SQL Interview Questions

## 🔹 Find Second Highest Salary

```sql
SELECT MAX(salary) AS second_highest_salary
FROM employees
WHERE salary < (
    SELECT MAX(salary)
    FROM employees
);
```

---

## 🔹 Top 3 Highest Salaries

```sql
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 3;
```

---

## 🔹 Count Employees Department Wise

```sql
SELECT department,
       COUNT(*) AS total_employees
FROM employees
GROUP BY department;
```

---

## 🔹 Find Duplicate Records

```sql
SELECT name,
       COUNT(*) AS duplicate_count
FROM employees
GROUP BY name
HAVING COUNT(*) > 1;
```

---

# 📊 Case Study Practice

This project includes business case studies like:
- Customer Sales Analysis
- Product Performance Tracking
- Revenue Analysis
- Employee Database Analysis
- Customer Retention Insights

---

# 📈 Skills Improved

✅ SQL Query Writing  
✅ Data Analysis  
✅ Business Understanding  
✅ Problem Solving  
✅ Interview Preparation  

---

# 🔮 Future Improvements

- Add LeetCode SQL Solutions
- Add HackerRank SQL Practice
- Include Real Interview Questions
- Add Advanced Case Studies

---

# 👨‍💻 Author

## Pankaj Jadhav

- GitHub: https://github.com/Pankaj24112005
- LinkedIn: https://linkedin.com/

---

# ⭐ Support

If you found this project useful, give it a ⭐ on GitHub!
