import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "notifications.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS notifications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                time_info TEXT NOT NULL,
                ip_address TEXT,
                extra TEXT
            )
        """)
        conn.commit()

def update_db_structure():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("ALTER TABLE notifications ADD COLUMN created_at TIMESTAMP")
            conn.commit()
        except sqlite3.OperationalError as e:
            if 'duplicate column name' in str(e):
                print("Столбец created_at уже существует.")
            else:
                raise e

if __name__ == "__main__":
    init_db()
    update_db_structure()