# 🚀 Day 71 – Multiple Linear Regression

## Project Overview
This project is part of my #100DaysOfCode challenge.

In Day 71, I implemented **Multiple Linear Regression from scratch**
using the Normal Equation on a real-world Housing Price dataset.

The goal was to understand how multiple independent variables
influence a target variable (house price).

---

##  Dataset

Dataset Used:
Housing Price Dataset (Kaggle - jenyraja)

Columns:
- price (Target)
- area
- bedrooms
- bathrooms
- stories
- mainroad
- guestroom
- basement
- hotwaterheating
- airconditioning
- parking
- prefarea
- furnishingstatus

Total Rows: 545
Total Columns: 13

---

##  Data Preprocessing

✔ Encoded binary categorical columns:
  - yes → 1
  - no → 0

✔ Applied One-Hot Encoding:
  - furnishingstatus

✔ Performed Train-Test Split (80-20)

✔ Applied StandardScaler for feature scaling

---

## Model Implementation

Implemented Multiple Linear Regression using:

Normal Equation:
θ = (XᵀX)^(-1) Xᵀy

Used:
np.linalg.pinv()  (Pseudo-inverse for stability)

Added bias term manually.

---

## Evaluation Metrics

- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

Visualization:
Actual vs Predicted Scatter Plot

---

## Key Learnings

- Handling mixed data types (numerical + categorical)
- Feature encoding techniques
- Importance of feature scaling
- Matrix operations in NumPy
- Avoiding singular matrix issues
- Understanding how coefficients change with multiple features

---

## 🛠️ Tech Stack

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn (for preprocessing only)

---

## File Structure

Day_71_Multiple_Linear_Regression.ipynb
README.md
housing.csv

---

## Future Improvements

- Implement Gradient Descent version
- Add correlation heatmap
- Check multicollinearity using VIF
- Try regularization (Ridge / Lasso)

---

## GitHub Repository

https://github.com/Pankaj24112005/100_Days_Coding_Challenge-

---

🔥 Consistency > Motivation  
Day 71/100 Complete
