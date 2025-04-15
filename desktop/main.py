import sys
from PyQt5.QtWidgets import QApplication
from window import FramelessMainWindow

def main():
    app = QApplication(sys.argv)
    window = FramelessMainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()