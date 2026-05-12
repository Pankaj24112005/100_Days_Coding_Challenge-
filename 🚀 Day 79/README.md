# 🚀 Day 79 – Bias–Variance Tradeoff

This project is part of my **#100DaysOfCode Machine Learning Journey**.

Today I learned about the **Bias–Variance Tradeoff**, one of the most important concepts in Machine Learning for building models that generalize well on unseen data.

---

## 📌 What is Bias?

Bias refers to the error caused by overly simple assumptions in a learning algorithm.

High bias can cause the model to miss important relationships in the data.

➡ Result: **Underfitting**

Example:
A linear model trying to learn a complex nonlinear relationship.

---

## 📌 What is Variance?

Variance refers to how sensitive a model is to small fluctuations in the training data.

A model with high variance learns the training data too well, including noise.

➡ Result: **Overfitting**

Example:
A very complex polynomial model that perfectly fits training data but fails on new data.

---

## ⚖️ Bias–Variance Tradeoff

A good machine learning model should balance **bias and variance**.

| Scenario      | Problem             |
| ------------- | ------------------- |
| High Bias     | Underfitting        |
| High Variance | Overfitting         |
| Balanced      | Good Generalization |

The goal is to **minimize total error** by finding the right balance.

---

## 🧪 Implementation in This Notebook

In this notebook, I demonstrated:

* Creating a synthetic dataset
* Training polynomial regression models
* Visualizing **underfitting**
* Visualizing **balanced fitting**
* Visualizing **overfitting**

Polynomial degrees used:

* Degree 1 → **Underfitting (High Bias)**
* Degree 4 → **Balanced Model**
* Degree 15 → **Overfitting (High Variance)**

---

## 🛠 Technologies Used

* Python
* NumPy
* Matplotlib
* Scikit-learn
* Jupyter Notebook

---

## 📂 Project Structure

```
Day 79 Bias Variance Tradeoff
│
├── day79_bias_variance_tradeoff.ipynb
└── README.md
```

---

## 🎯 Key Learning

The **Bias–Variance Tradeoff** helps us understand why some models:

* perform poorly on training data (underfitting)
* perform well on training but poorly on test data (overfitting)

Balancing bias and variance leads to **better generalization and more reliable machine learning models**.

⭐ If you found this helpful, feel free to **star the repository**.
