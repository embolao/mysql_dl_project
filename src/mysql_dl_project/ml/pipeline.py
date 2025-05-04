import pandas as pd

from .db import get_connection


def load_data():
    with get_connection() as conn:
        df = pd.read_sql("SELECT * FROM users", conn)
    df["target"] = (df["age"] > 30).astype(int)
    return df
