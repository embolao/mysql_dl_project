import os

import joblib

# import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from ..utils.logging import append_log
from .pipeline import load_data

os.makedirs("outputs", exist_ok=True)


def train_model():
    df = load_data()
    X = df[["age"]].values
    y = df["target"].values

    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    joblib.dump(model, "outputs/model_sklearn.pkl")

    append_log(
        "sklearn",
        "train",
        f"Coef: {model.coef_.tolist()} | Intercept: {model.intercept_.tolist()}",
    )
    print("✅ Modelo sklearn guardado.")


def predict_model(age):
    model = joblib.load("outputs/model_sklearn.pkl")
    prediction = model.predict([[age]])[0]
    prob = model.predict_proba([[age]])[0][1]

    append_log(
        "sklearn",
        "predict",
        f"Age: {age}, Prediction: {prediction}, Probability: {prob:.2f}",
    )
    print(f"🔎 Predicción sklearn para edad {age}: {prediction} (score: {prob:.2f})")


def inspect_model():
    model = joblib.load("outputs/model_sklearn.pkl")
    coef = model.coef_.tolist()
    intercept = model.intercept_.tolist()

    with open("outputs/inspect_sklearn.txt", "w") as f:
        f.write(f"Coeficientes: {coef}\n")
        f.write(f"Intercepción: {intercept}\n")

    append_log("sklearn", "inspect", "Modelo inspeccionado y exportado.")
    print("✅ Detalles del modelo guardados en 'inspect_sklearn.txt'")
