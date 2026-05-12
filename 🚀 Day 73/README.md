# Day 73 – Logistic Regression (Implementation from Scratch)

## Project Overview

This project implements **Logistic Regression from scratch using Python** on the Titanic dataset.

Instead of using `sklearn`, the model is built manually using:

- Sigmoid Function
- Log Loss (Binary Cross-Entropy)
- Gradient Descent
- Weight & Bias Updates
- Probability Thresholding

This strengthens understanding of the mathematics behind classification models.

---

## Dataset

Dataset Used: Titanic (train_and_test2.csv)

Target Column:
- `Survived` (renamed from `2urvived`)
  - 0 → Did Not Survive
  - 1 → Survived

Initial Dataset Shape:
- 1309 rows
- 28 columns

---

## Data Cleaning Steps

- Removed unnecessary columns (`zero`, `zero.1`, ..., `zero.18`)
- Renamed `2urvived` → `Survived`
- Filled missing values in `Embarked`
- Selected important features only
- Applied feature normalization

Selected Features:
- Pclass
- Sex
- Age
- Fare
- sibsp
- Parch
- Embarked

---

## Model Implementation

### 1. Sigmoid Function
sigma(z) = 1 / (1 + e^(-z))

### 2. Forward Propagation
z = XW + b  
y_pred = sigmoid(z)

### 3. Loss Function (Log Loss)
Loss = - (1/m) Σ [ y log(y_hat) + (1 - y) log(1 - y_hat) ]

### 4. Gradient Descent
Weights and bias updated using partial derivatives.

---

## Results

- Model trained using full dataset
- Accuracy calculated on training data
- Implemented without sklearn

---

## Why This Project Matters

- Builds strong ML fundamentals
- Improves mathematical intuition
- Prepares for ML interviews
- Demonstrates ability to implement algorithms from scratch
- Moves beyond just using libraries

---

## Next Step

Day 74 – Add Train/Test Split, Confusion Matrix, and Evaluation Metrics

---

#100DaysOfCode  
#MachineLearning  
#LogisticRegression  
#AI  
#DataScience  
