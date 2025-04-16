import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from window import FramelessMainWindow
from database.db import init_db, add_notification   

def main():
    init_db()

    app = QApplication(sys.argv)
    
    icon_path = os.path.join(os.path.dirname(__file__), "assets", "logo.ico")
    app.setWindowIcon(QIcon(icon_path))

    window = FramelessMainWindow()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
