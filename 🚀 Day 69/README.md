Day 69 – Linear Regression (Implementation from Scratch)

Overview:
On Day 69 of my 100 Days of Code journey, I implemented Linear Regression from scratch using Python without using any machine learning libraries.

The goal was to deeply understand:
- Hypothesis function
- Cost Function (Mean Squared Error)
- Gradient Descent
- Parameter updates (Weight & Bias)
- Model convergence

Concepts Covered:

1) Hypothesis Function
y_hat = wX + b
w = weight (slope)
b = bias (intercept)

2) Cost Function (Mean Squared Error)
J(w, b) = (1 / 2m) * sum((y_hat - y)^2)

3) Gradient Descent Update Rule
w = w - alpha * dJ/dw
b = b - alpha * dJ/db
alpha = learning rate

Project Structure:

Day_69/
|-- Day_69_Linear_Regression_Implementation.ipynb
|-- README.md

Implementation Steps:

1. Created a simple dataset (Hours vs Scores)
2. Initialized parameters (w, b)
3. Implemented cost function manually
4. Applied gradient descent
5. Visualized regression line and cost reduction

Technologies Used:
- Python
- NumPy
- Matplotlib

GitHub:
https://github.com/Pankaj24112005/100_Days_Coding_Challenge-/tree/main/%F0%9F%9A%80%20Day%2069

#MachineLearning #LinearRegression #Python #DataScience #100DaysOfCode
