import sqlite3
from pathlib import Path
from datetime import datetime

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
                extra TEXT,
                created_at TEXT NOT NULL
            )
        """)
        conn.commit()

def get_notifications():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT title, time_info, ip_address, extra, created_at FROM notifications ORDER BY id DESC")
        return cursor.fetchall()

def add_notification(title, time_info, ip_address=None, extra=None):
    created_at = datetime.now().isoformat()
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO notifications (title, time_info, ip_address, extra, created_at)
            VALUES (?, ?, ?, ?, ?)
        """, (title, time_info, ip_address, extra, created_at))
        conn.commit()

def clear_notifications():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notifications")
    conn.commit()
    conn.close()

def delete_notification_by_title(title):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM notifications WHERE title = ?", (title,))
        conn.commit()
