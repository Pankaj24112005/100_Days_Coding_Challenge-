# Day 67 – Train-Test Split  
## 100 Days of Coding Challenge

Today’s focus was on understanding and implementing **Train-Test Split**, one of the most fundamental steps in any Machine Learning workflow.

---

## 📌 Objective

Learn how to split a dataset into:

- **Training Set** – used to train the model  
- **Testing Set** – used to evaluate model performance on unseen data  

This helps ensure that our model generalizes well and does not simply memorize the dataset.

---

## Tools Used

- Python  
- Pandas  
- Scikit-learn  

---

## Files Included

- `Day67_Train_Test_Split.ipynb` – Jupyter Notebook with implementation  
- `README.md` – Project documentation  

---

## What I Learned

✅ Importance of separating training and testing data  
✅ How to use `train_test_split()` from `sklearn`  
✅ Understanding `test_size` and `random_state`  
✅ Why model evaluation on unseen data matters  

---

## 🧪 Sample Code

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
