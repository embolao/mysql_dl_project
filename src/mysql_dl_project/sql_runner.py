from mysql_dl_project.ml.db import get_connection


def run_sql(query):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results
