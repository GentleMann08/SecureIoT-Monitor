import sqlite3
from pathlib import Path
from datetime import datetime

DB_PATH = Path(__file__).resolve().parent / "users.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                username TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        """)
        conn.commit()


def get_users():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT first_name, last_name, username, created_at FROM users ORDER BY id DESC")
        return cursor.fetchall()
    
    
def add_user(first_name, last_name, username):
    created_at = datetime.now().isoformat()

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            cursor.execute("""
                UPDATE users
                SET first_name = ?, last_name = ?, created_at = ?
                WHERE username = ?
            """, (first_name, last_name, created_at, username))
        else:
            cursor.execute("""
                INSERT INTO users (first_name, last_name, username, created_at)
                VALUES (?, ?, ?, ?)
            """, (first_name, last_name, username, created_at))

        conn.commit()