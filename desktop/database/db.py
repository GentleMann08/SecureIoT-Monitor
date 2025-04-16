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


def get_notifications():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT title, time_info, ip_address, extra FROM notifications ORDER BY id DESC")
        return cursor.fetchall()


def add_notification(title, time_info, ip_address=None, extra=None):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO notifications (title, time_info, ip_address, extra)
            VALUES (?, ?, ?, ?)
        """, (title, time_info, ip_address, extra))
        conn.commit()

def clear_notifications():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notifications")
    conn.commit()
    conn.close()