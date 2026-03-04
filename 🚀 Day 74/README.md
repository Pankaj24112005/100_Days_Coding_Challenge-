# 🚀 Day 74 – Confusion Matrix & Evaluation Metrics

Part of my #100DaysOfCode Data Science Challenge

Today I learned how to evaluate classification models using the Confusion Matrix and important evaluation metrics. These metrics help us understand how well a machine learning model performs beyond simple accuracy.

-----------------------------------------------------

📌 What is a Confusion Matrix?

A Confusion Matrix is a table used to evaluate the performance of a classification model by comparing actual values with predicted values.

It consists of four key components:

TP (True Positive)   → Model correctly predicts the positive class
TN (True Negative)   → Model correctly predicts the negative class
FP (False Positive)  → Model predicts positive but actually negative
FN (False Negative)  → Model predicts negative but actually positive

-----------------------------------------------------

📊 Evaluation Metrics

1️⃣ Accuracy
Accuracy measures the overall correctness of the model.

Accuracy = (TP + TN) / Total Predictions


2️⃣ Precision
Precision measures how many predicted positive cases are actually correct.

Precision = TP / (TP + FP)


3️⃣ Recall (Sensitivity)
Recall measures the ability of the model to detect all actual positive cases.

Recall = TP / (TP + FN)


4️⃣ F1 Score
F1 Score balances Precision and Recall.

F1 Score = 2 × (Precision × Recall) / (Precision + Recall)

-----------------------------------------------------

🧠 Why These Metrics Matter

In real-world applications like:

• Healthcare diagnosis
• Fraud detection
• Spam filtering

Accuracy alone can be misleading. Precision, Recall, and F1 Score provide deeper insight into model performance.

-----------------------------------------------------

🛠 Tools & Libraries Used

Python
NumPy
Pandas
Scikit-learn
Jupyter Notebook

-----------------------------------------------------

📂 Project Structure

Day 74
│
├── confusion_matrix_metrics.ipynb
└── README.md

-----------------------------------------------------

🔗 GitHub Repository

https://github.com/Pankaj24112005/100_Days_Coding_Challenge-/tree/main/%F0%9F%9A%80%20Day%2074

-----------------------------------------------------

📅 Challenge Progress

This project is part of my 100 Days of Data Science & Machine Learning Journey where I practice concepts daily and share them publicly.

-----------------------------------------------------

#DataScience #MachineLearning #100DaysOfCode #Python #AI #LearningInPublic
