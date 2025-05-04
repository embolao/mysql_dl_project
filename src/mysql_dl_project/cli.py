import os

import click

from .ml.pytorch_model import inspect_model as torch_inspect
from .ml.pytorch_model import predict_model as torch_predict
from .ml.pytorch_model import train_model as torch_train
from .ml.sklearn_model import inspect_model as sk_inspect
from .ml.sklearn_model import predict_model as sk_predict
from .ml.sklearn_model import train_model as sk_train

# from .utils.logging import append_log


@click.group()
def cli():
    pass


# ----- PyTorch -----
@cli.command()
def train_torch():
    torch_train()


@cli.command()
@click.argument("age", type=float)
def predict_torch(age):
    torch_predict(age)


@cli.command()
def inspect_torch():
    torch_inspect()


# ----- Scikit-learn -----
@cli.command()
def train_sklearn():
    sk_train()


@cli.command()
@click.argument("age", type=float)
def predict_sklearn(age):
    sk_predict(age)


@cli.command()
def inspect_sklearn():
    sk_inspect()


# ----- Logs -----
@cli.command()
@click.option("--all", is_flag=True, help="Mostrar todos los logs.")
def view_logs(all):
    import os

    log_dir = "outputs/logs"
    os.makedirs(log_dir, exist_ok=True)
    found_logs = False

    for model_name in ["pytorch", "sklearn"]:
        path = os.path.join(log_dir, f"{model_name}.log")
        if os.path.exists(path):
            found_logs = True
            print(f"\n📄 Logs de {model_name.capitalize()}:\n{'-'*30}")
            with open(path) as f:
                lines = f.readlines()
                if all:
                    print("".join(lines))
                else:
                    print("".join(lines[-5:]))

    if not found_logs:
        print("❌ No se encontraron logs.")


# ----- Limpiar logs -----
@cli.command()
def clear_logs():
    log_dir = "outputs/logs"
    os.makedirs(log_dir, exist_ok=True)
    for model_name in ["pytorch", "sklearn"]:
        path = os.path.join(log_dir, f"{model_name}.log")
        if os.path.exists(path):
            os.remove(path)
            print(f"✅ Logs de {model_name.capitalize()} eliminados.")
        else:
            print(f"❌ No se encontraron logs de {model_name.capitalize()}.")
