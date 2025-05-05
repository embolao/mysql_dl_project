from tabulate import tabulate
from termcolor import colored

from mysql_dl_project.ml.db import get_connection


def run_sql(query):
    """Ejecuta una consulta SQL y devuelve los resultados formateados en una tabla."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query)

        query_type = query.strip().lower().split()[0]

        # Si la consulta no es SELECT (modificación de datos), no mostramos la tabla
        if query_type in ("insert", "update", "delete", "create", "drop", "alter"):
            conn.commit()
            return []

        try:
            rows = cursor.fetchall()
            headers = [desc[0] for desc in cursor.description]

            # Color de encabezado
            colored_headers = [colored(header, "yellow") for header in headers]

            # Colores para las filas
            colored_rows = []
            for row in rows:
                colored_row = []
                for value in row:
                    # Cambiar color dependiendo del tipo de dato
                    if isinstance(value, int):
                        colored_row.append(colored(value, "green"))
                    elif isinstance(value, str):
                        colored_row.append(colored(value, "cyan"))
                    else:
                        colored_row.append(colored(value, "white"))
                colored_rows.append(colored_row)

            # Imprimir solo la tabla con colores
            print(tabulate(colored_rows, headers=colored_headers, tablefmt="grid"))
            return []  # Regresamos una lista vacía para evitar imprimir las tuplas
        except Exception as e:
            print(f"❌ Error: {e}")
            return []
