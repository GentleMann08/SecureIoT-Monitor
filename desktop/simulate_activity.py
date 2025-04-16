import sqlite3
from pathlib import Path
import time
import random
from datetime import datetime

DB_PATH = Path(__file__).resolve().parent / "database/notifications.db"

def add_notification(title, ip_address=None, extra=None):
    created_at = datetime.now().isoformat()
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO notifications (title, time_info, ip_address, extra, created_at)
            VALUES (?, ?, ?, ?, ?)
        """, (title, "Системное уведомление", ip_address, extra, created_at))
        conn.commit()

def generate_random_notification():
    titles = [
        "Обнаружено подозрительное устройство",
        "Несанкционированное подключение",
        "Попытка взлома",
        "Нестандартный порт открыт"
    ]
    ip_addresses = [
        "192.168.0.234",
        "192.168.0.123",
        "192.168.1.56",
        "192.168.1.78"
    ]
    extras = [
        "нестандартный порт",
        "многочисленные попытки подключения",
        "неизвестное устройство",
        "подозрительный трафик"
    ]

    title = random.choice(titles)
    ip_address = random.choice(ip_addresses)
    extra = random.choice(extras)

    return title, ip_address, extra

def simulate_activity():
    while True:
        title, ip_address, extra = generate_random_notification()
        add_notification(title, ip_address, extra)
        print(f"Добавлено уведомление: {title}, {ip_address}, {extra}")
        time.sleep(30)

if __name__ == "__main__":
    simulate_activity()
