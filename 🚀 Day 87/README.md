# 📊 Customer Personality Analysis (EDA Project)

## 🚀 Project Overview
This project focuses on performing **Exploratory Data Analysis (EDA)** on a real-world marketing dataset to understand customer behavior, spending patterns, and key business insights.

The goal is to extract meaningful information that can help businesses make **data-driven marketing decisions**.

---

## 📁 Dataset
- Source: Kaggle  
- Dataset Name: **Customer Personality Analysis**  
- Format: CSV (Tab-separated)

---

## 🎯 Objectives
- Understand customer demographics and behavior  
- Analyze spending patterns across product categories  
- Identify relationships between income, age, and spending  
- Perform feature engineering for deeper insights  

---

## 🛠️ Tools & Technologies
- Python 🐍  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Jupyter Notebook  

---

## 🔧 Project Workflow

### 1️⃣ Data Loading
- Imported dataset using Pandas
- Checked structure using .info(), .describe()

### 2️⃣ Data Cleaning
- Handled missing values (Income column)
- Fixed date format issues using pd.to_datetime()
- Converted data types

### 3️⃣ Feature Engineering
- Created new features:
  - Age from Year_Birth  
  - Total Spending from product categories  
  - Family Size from household data  

### 4️⃣ Exploratory Data Analysis
- Univariate Analysis (Age, Income)  
- Bivariate Analysis (Income vs Spending, Education vs Spending)  
- Correlation Analysis (Heatmap)  

### 5️⃣ Visualization
- Histograms  
- Scatter plots  
- Box plots  
- Heatmaps  

---

## 📊 Key Insights
- Customers with higher income tend to spend more  
- Wine and meat products contribute most to total spending  
- Family size impacts purchasing behavior  
- Education level influences spending patterns  
- Middle-aged customers are more active buyers  

---

## 💡 Business Recommendations
- Target high-income customers with premium products  
- Create personalized offers based on family size  
- Focus marketing campaigns on high-spending categories  
- Segment customers for better engagement  

---

## 📁 Project Structure

EDA-Customer-Analysis/
│
├── EDA_Customer_Analysis.ipynb
├── marketing_campaign.csv
├── cleaned_customer_data.csv
└── README.md

---

## ▶️ How to Run

git clone https://github.com/your-username/EDA-Customer-Analysis.git

pip install pandas numpy matplotlib seaborn

jupyter notebook

---

## 🚀 Future Improvements
- Customer segmentation using K-Means  
- Power BI / Streamlit dashboard  
- Deploy as a web application  

---

## 📌 Author
Pankaj Jadhav  
AI & Data Science Student  

---

## ⭐ If you like this project
Give it a star ⭐ and connect!
