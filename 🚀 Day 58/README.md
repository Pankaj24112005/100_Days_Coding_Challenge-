# 🚀 Day 58 – Univariate Analysis  
### 100 Days of Data Science Challenge  

## 📌 Objective  
The goal of Day 58 is to perform **Univariate Analysis** to understand individual features in a dataset using statistical summaries and visualizations before moving into deeper Exploratory Data Analysis (EDA).

---

## 📂 Dataset Columns  

- Id  
- EmployeeName  
- JobTitle  
- BasePay  
- OvertimePay  
- OtherPay  
- Benefits  
- TotalPay  
- TotalPayBenefits  
- Year  
- Notes  
- Agency  
- Status  

---

## 🔧 Tools & Libraries Used  

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Jupyter Notebook / VS Code  

---

## 📊 Operations Performed  

### ✅ Data Understanding  
- Loaded dataset  
- Checked shape and column information  
- Identified numerical and categorical features  

### ✅ Statistical Summary  
- Used `describe()` for numerical columns  
- Used `value_counts()` for categorical columns  
- Calculated mean, median, and mode  

### ✅ Univariate Visualizations  

#### Numerical Features  
- Histogram for salary-related columns  
- Boxplot for outlier detection  

Columns analyzed:  
- BasePay  
- OvertimePay  
- OtherPay  
- Benefits  
- TotalPay  
- TotalPayBenefits  

#### Categorical Features  
- Bar chart for JobTitle vs Average BasePay  

---

## 🚨 Data Cleaning  

- Converted `BasePay` from object to numeric using:

```python
pd.to_numeric(errors="coerce")
