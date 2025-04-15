import sys
from PyQt5.QtWidgets import QApplication
from window import FramelessMainWindow
from database.db import init_db
from database.db import add_notification

def main():
    init_db()
    
    add_notification("Обнаружено подозрительное устройство, IP: 192.168.0.234", "Системное уведомление • 3 мин назад", "192.168.0.234")
    add_notification("Несанкционированное подключение", "Системное уведомление • 1 мин назад", "192.168.0.123", "нестандартный порт")

    app = QApplication(sys.argv)
    window = FramelessMainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()