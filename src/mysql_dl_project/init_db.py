import click
import mysql.connector


@click.command()
def init_db():
    """Inicializa la base de datos y la tabla users con datos."""
    conn = mysql.connector.connect(
        host="localhost",
        user="user",
        password="password",
        database="dl_data",
        port=3306,
    )
    cursor = conn.cursor()

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100),
        age INT
    );
    """
    )

    cursor.executemany(
        """
    INSERT INTO users (name, email, age)
    VALUES (%s, %s, %s)
    """,
        [
            ("Alice", "alice@example.com", 28),
            ("Bob", "bob@example.com", 35),
            ("Charlie", "charlie@example.com", 40),
        ],
    )

    conn.commit()
    cursor.close()
    conn.close()
    click.echo("✅ Base de datos inicializada.")
