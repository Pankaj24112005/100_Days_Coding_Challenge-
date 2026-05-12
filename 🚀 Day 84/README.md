# 🚀 Day 84 – Elbow Method & Silhouette Score

This project is part of my **#100DaysOfCoding Challenge**, where I learn and implement concepts from **Data Science and Machine Learning** every day.

## 📌 Topic: Elbow Method & Silhouette Score

When using clustering algorithms like **K-Means**, it is important to determine the **optimal number of clusters (K)**.  
Two common techniques used for this are:

- **Elbow Method**
- **Silhouette Score**

These methods help evaluate the quality of clustering.

---

## 📊 Elbow Method

The **Elbow Method** helps determine the best number of clusters by plotting:

**Number of Clusters (K) vs WCSS (Within-Cluster Sum of Squares)**

Steps:
1. Run K-Means for different values of **K**
2. Calculate **WCSS** for each K
3. Plot the graph
4. The point where the curve bends like an **elbow** indicates the optimal K

---

## 📈 Silhouette Score

The **Silhouette Score** measures how well a data point fits within its cluster.

Score range:
- **+1 → Well clustered**
- **0 → Overlapping clusters**
- **-1 → Wrong clustering**

Higher silhouette score means **better cluster separation**.

---

## 🧪 What This Notebook Does

- Creates a synthetic dataset using `make_blobs`
- Applies **K-Means clustering**
- Uses the **Elbow Method** to find optimal K
- Calculates **Silhouette Scores** for different cluster values

---

## 🛠️ Technologies Used

- Python
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

---

## 📂 Project Structure

```
Day 84
 ├── day84_elbow_silhouette.ipynb
 └── README.md
```

---

## ▶️ How to Run

1️⃣ Clone the repository

```bash
git clone https://github.com/Pankaj24112005/100_Days_Coding_Challenge-.git
```

2️⃣ Install required libraries

```bash
pip install numpy matplotlib scikit-learn
```

3️⃣ Run the notebook

```bash
jupyter notebook
```

---

## 🔗 GitHub Repository

https://github.com/Pankaj24112005/100_Days_Coding_Challenge-/tree/main/%F0%9F%9A%80%20Day%2084

---

## 📅 Challenge Progress

**Day 84 / 100 – Improving clustering evaluation skills in Machine Learning**

---

⭐ Follow my journey as I explore **Data Science, Machine Learning, and AI** through the **#100DaysOfCoding challenge**.

#MachineLearning #DataScience #Python #KMeans #Clustering #AI #100DaysOfCode
