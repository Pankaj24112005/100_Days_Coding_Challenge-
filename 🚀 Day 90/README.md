# Heart Disease Prediction (Pickle and Joblib ML Project)

## Overview

This project predicts whether a person has heart disease or not using Machine Learning.
It demonstrates a **complete ML workflow** including data preprocessing, model training, pipeline creation, and model saving using **Pickle** and **Joblib**.

---

##  Features

* Real dataset (`heart.csv`)
* Data preprocessing,
* Machine Learning model (Logistic Regression)
* Pipeline (StandardScaler + Model) ⭐
* Model saving using Pickle & Joblib
* Model loading and prediction
* Confidence score output

---

## Project Structure

```
heart-disease-prediction-pipeline/
│
├── data/
│   └── heart.csv
│
├── notebook/
│   └── heart_disease_kaggle_project.ipynb
│
├── models/
│   ├── heart_model.pkl
│   └── heart_model.joblib
│
├── app/   (optional)
│   └── app.py
│
└── README.md
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Pickle
* Joblib

---

## How It Works

1. Load dataset
2. Split into training and testing data
3. Create pipeline:

   * StandardScaler (for feature scaling)
   * Logistic Regression (for classification)
4. Train model
5. Evaluate accuracy
6. Save model using Pickle & Joblib
7. Load model and make predictions

---

## Model Saving

```python
import pickle
import joblib

# Save
pickle.dump(pipeline, open("heart_model.pkl", "wb"))
joblib.dump(pipeline, "heart_model.joblib")

# Load
model = joblib.load("heart_model.joblib")
```

---

## Prediction Example

```python
result, prob = predict_with_confidence(model, sample)

print("Prediction:", result)
print(f"Confidence: {prob*100:.2f}%")
```

---

## Output Example

```
Prediction: Person HAS heart disease
Confidence: 82.34%
```

---

## Key Learning

* Importance of Pipelines in ML
* Difference between Pickle and Joblib
* Saving complete ML workflow
* Converting predictions into human-readable output
* Adding confidence scores

---

## Future Improvements

* Add EDA & visualization
* Try multiple ML models
* Hyperparameter tuning
* Deploy using Flask / FastAPI
* Build UI using Streamlit

---

## Connect with Me

If you like this project, feel free to connect and give feedback!

🔗 GitHub: https://github.com/Pankaj24112005
🔗 LinkedIn: (Add your profile link)

---

## Star This Repo

If you found this helpful, give it a ⭐ on GitHub!
