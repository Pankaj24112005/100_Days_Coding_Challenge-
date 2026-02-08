# 🚀 Day 51 – SQL GROUP BY & HAVING

Welcome to **Day 51** of my **100 Days Coding Challenge**!

Today I learned two powerful SQL concepts used in data analysis:

👉 GROUP BY  
👉 HAVING  

These help summarize large datasets and filter aggregated results.

---

## 📚 Topics Covered

✅ GROUP BY clause  
✅ Aggregate Functions (COUNT, SUM, AVG, MIN, MAX)  
✅ GROUP BY with multiple columns  
✅ HAVING clause  
✅ Difference between WHERE vs HAVING  
✅ Analytical queries

---

## 🧠 Key Concepts

### 🔹 GROUP BY
Groups rows with similar values.

```sql
SELECT department, COUNT(*)  
FROM employees  
GROUP BY department;
```

---

### 🔹 HAVING
Filters grouped results.

```sql
SELECT department, COUNT(*)  
FROM employees  
GROUP BY department  
HAVING COUNT(*) > 2;
```

---

## 🔥 WHERE vs HAVING

| WHERE | HAVING |
|------|--------|
| Filters rows | Filters groups |
| Used before GROUP BY | Used after GROUP BY |
| Cannot use aggregates | Can use aggregates |

---
## 🎯 What I Learned

✔ Data summarization using GROUP BY  
✔ Filtering grouped data with HAVING  
✔ Writing analytical SQL queries  
✔ Understanding aggregation logic  

---

## 💡 Why This Matters

Used in:

📌 Data Analytics  
📌 Business Intelligence  
📌 Machine Learning preprocessing  
📌 Dashboards  

---

## 🚀 Next Goal

Advanced SQL + real-world datasets.

---

### 📌 Part of #100DaysCodingChallenge  
Let’s keep learning! 💪
