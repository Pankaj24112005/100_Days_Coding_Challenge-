# End-to-End House Price Prediction using Regression

##  Project Overview
This project focuses on building a machine learning regression model to predict house prices based on various features such as area, quality, and structural attributes.

The project follows a complete data science pipeline including data preprocessing, feature selection, model training, and evaluation.

---

## Objective
- Predict house prices using regression techniques  
- Perform Exploratory Data Analysis (EDA)  
- Handle missing values and clean the dataset  
- Evaluate model performance using standard metrics  

---

## Dataset
- Dataset: House Prices - Advanced Regression Techniques (Kaggle)  
- Target Variable: `SalePrice`  

---

## ⚙️ Technologies Used
- Python 
- NumPy  
- Pandas  
- Matplotlib  
- Seaborn  
- Scikit-learn  

---

## Project Workflow

### 1. Data Loading
- Imported dataset using Pandas  

### 2. Data Exploration
- Checked dataset structure using `.info()` and `.describe()`  
- Visualized correlations using heatmap  

### 3. Data Cleaning
- Removed columns with excessive missing values  
- Filled missing values using median strategy  

### 4. Feature Selection
- Selected top correlated features with target variable  

### 5. Model Building
- Used Linear Regression model  
- Split data into training and testing sets  

### 6. Model Evaluation
- Evaluated using:  
  - MAE (Mean Absolute Error)  
  - MSE (Mean Squared Error)  
  - RMSE (Root Mean Squared Error)  
  - R² Score  

### 7. Prediction
- Tested model on random unseen data points  

---

## Results
- The model successfully predicts house prices with reasonable accuracy  
- Demonstrates strong understanding of regression workflow  

---

## Sample Output
- Actual vs Predicted Price comparison  
- Residual distribution plot  

---

##  Future Improvements
- Implement Ridge and Lasso Regression  
- Perform feature scaling  
- Use advanced models (Random Forest, XGBoost)  
- Deploy as a web application using Streamlit  

---

##  Project Structure
House-Price-Prediction  
 ┣ train.csv  
 ┣ README.md  
 ┣ regression_project.ipynb  

---

## Key Learnings
- End-to-end machine learning workflow  
- Feature engineering and selection  
- Model evaluation techniques  
- Real-world dataset handling  

---

##  Author
**Pankaj J**  
Aspiring AI/ML Engineer 🚀  

---

##  Acknowledgement
Dataset provided by Kaggle for educational and research purposes.
