import sqlite3

def connect_db():
    return sqlite3.connect("tickets.db")


def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        issue TEXT,
        priority TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()
