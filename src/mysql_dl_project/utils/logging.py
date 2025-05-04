import os
from datetime import datetime

LOG_DIR = "outputs/logs"
os.makedirs(LOG_DIR, exist_ok=True)


def append_log(model_name: str, operation: str, content: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{operation.upper()}] {content}\n"
    log_path = os.path.join(LOG_DIR, f"{model_name}.log")

    with open(log_path, "a") as f:
        f.write(log_entry)
