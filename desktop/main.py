import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from window import FramelessMainWindow
from database.db import init_db, add_notification
from PyQt5.QtGui import QPixmap

def main():
    init_db()
    
    add_notification("Обнаружено подозрительное устройство, IP: 192.168.0.234", "Системное уведомление • 3 мин назад", "192.168.0.234")
    add_notification("Несанкционированное подключение", "Системное уведомление • 1 мин назад", "192.168.0.123", "нестандартный порт")

    app = QApplication(sys.argv)
    
    icon_path = os.path.join(os.path.dirname(__file__), "assets", "logo.ico")
    app.setWindowIcon(QIcon(icon_path))

    window = FramelessMainWindow()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
