from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from ui.header import Header
from ui.sidebar import Sidebar
from ui.content import Content
from widgets.window_controls import WindowControls
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import os

class FramelessMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IOT Security Monitor")
        self.setGeometry(100, 100, 1000, 600)
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Устанавливаем иконку окна
        icon_path = os.path.join(os.path.dirname(__file__), "assets", "logo.ico")
        self.setWindowIcon(QIcon(icon_path))
        
        self.offset = None

        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        self.header = Header(self)
        main_layout.addWidget(self.header)

        body_layout = QHBoxLayout()
        body_layout.setContentsMargins(0, 0, 0, 0)
        body_layout.setSpacing(0)

        self.sidebar = Sidebar()
        body_layout.addWidget(self.sidebar)

        self.content = Content()
        body_layout.addWidget(self.content)

        main_layout.addLayout(body_layout)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f2f5;
            }
            QFrame#Header {
                background-color: #2f2f2f;
            }
            QFrame#Sidebar {
                background-color: #3a3a3a;
            }
            QFrame#Content {
                background-color: #f0f2f5;
            }
        """)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event):
        if self.offset and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.offset)

    def mouseReleaseEvent(self, event):
        self.offset = None
