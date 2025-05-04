import os

import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split

from ..utils.logging import append_log
from .pipeline import load_data

os.makedirs("outputs", exist_ok=True)


class AgeClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(1, 8), nn.ReLU(), nn.Linear(8, 1), nn.Sigmoid()
        )

    def forward(self, x):
        return self.model(x)


def train_model():
    df = load_data()
    X = df[["age"]].values.astype("float32")
    y = df["target"].values.astype("float32")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    X_train = torch.tensor(X_train)
    y_train = torch.tensor(y_train).view(-1, 1)

    model = AgeClassifier()
    criterion = nn.BCELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)

    losses = []
    for epoch in range(100):
        model.train()
        optimizer.zero_grad()
        outputs = model(X_train)
        loss = criterion(outputs, y_train)
        loss.backward()
        optimizer.step()
        losses.append(loss.item())
        if epoch % 10 == 0:
            print(f"Epoch {epoch}: loss = {loss.item():.4f}")

    torch.save(model.state_dict(), "outputs/model_torch.pt")

    plt.plot(losses)
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title("Training Loss")
    plt.savefig("outputs/loss.png")

    append_log("pytorch", "train", f"Final loss: {loss.item():.4f}")
    print("✅ Modelo y gráfico guardados.")


def predict_model(age):
    model = AgeClassifier()
    model.load_state_dict(torch.load("outputs/model_torch.pt"))
    model.eval()

    with torch.no_grad():
        input_tensor = torch.tensor([[age]], dtype=torch.float32)
        output = model(input_tensor).item()
        pred = 1 if output >= 0.5 else 0
        append_log(
            "pytorch", "predict", f"Age: {age}, Prediction: {pred}, Score: {output:.2f}"
        )
        print(f"🔎 Predicción para edad {age}: {pred} (score: {output:.2f})")


def inspect_model():
    model = AgeClassifier()
    model.load_state_dict(torch.load("outputs/model_torch.pt"))
    model.eval()
    output_lines = ["📊 Modelo PyTorch (estructura y pesos):\n"]

    for name, param in model.named_parameters():
        values = param.data.numpy().flatten()
        output_lines.append(f"{name}: {values.tolist()}\n")

    with open("outputs/inspect_torch.txt", "w") as f:
        f.writelines(output_lines)

    append_log("pytorch", "inspect", "Modelo inspeccionado y exportado.")
    print("✅ Detalles del modelo guardados en 'inspect_torch.txt'")
