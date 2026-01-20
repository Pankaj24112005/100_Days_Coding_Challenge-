# 📅 Day 32 – Reading & Writing Data (CSV, Excel, JSON)

This repository contains hands-on examples of reading and writing data using **Python (pandas)**.  
These operations are fundamental in **Data Science, Machine Learning, and AI projects**, where data comes from multiple formats.

---

## 📌 Topics Covered

✅ Reading CSV files using `pandas.read_csv()`  
✅ Writing data to CSV using `to_csv()`  
✅ Reading & writing Excel files using `read_excel()` and `to_excel()`  
✅ Working with JSON data using `read_json()` and `to_json()`  
✅ Handling missing values while importing data  
✅ Understanding **when to use CSV vs Excel vs JSON**

---

## 🛠️ Technologies Used

- Python 🐍  
- Pandas 📊  
- Jupyter Notebook 📓  

---

## 📂 Files in This Folder

- `Day_32_Reading_Writing_Data.ipynb` → Main notebook with all examples  
- `.csv` files → Sample datasets  
- `.json` files → Sample JSON data  
- Generated files:
  - `output_csv.csv`
  - `output_excel.xlsx`
  - `output_json.json`

---

## 🚀 Key Code Examples

### Read CSV File
```python
import pandas as pd
df = pd.read_csv("data.csv")
df.head()

### Convert CSV to Excel
```python
df.to_excel("data.xlsx", index=False)
