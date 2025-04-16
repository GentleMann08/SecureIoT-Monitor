from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame, QWidget, QTextEdit
from PyQt5.QtCore import Qt, QDateTime, pyqtSignal
from PyQt5.QtGui import QPixmap, QTextOption
from database.db import delete_notification_by_title
from styles.stylesheet import DARK_BUTTON_STYLE

class NotificationDetailsWindow(QDialog):
    notification_deleted = pyqtSignal(str)

    def __init__(self, title, created_at, ip, extra):
        super().__init__()
        self.drag_position = None
        self.setWindowTitle(title)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("""
            QDialog {
                background-color: #1e1e1e;
                border-radius: 8px;
            }
            QLabel {
                color: #dddddd;
                font-size: 13px;
            }
            QFrame#Sidebar {
                background-color: #2c2c2c;
                border-radius: 8px;
            }
            QWidget#TopBar {
                background-color: #3c3c3c;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
            }
            QTextEdit {
                background-color: #2c2c2c;
                color: #dddddd;
                border: none;
                font-size: 13px;
            }
        """)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        top_bar = QWidget()
        top_bar.setObjectName("TopBar")
        top_bar.setFixedHeight(40)

        top_bar_layout = QHBoxLayout()
        top_bar_layout.setContentsMargins(10, 0, 10, 0)
        top_bar_layout.setSpacing(10)

        icon = QLabel()
        icon.setPixmap(QPixmap("assets/icons/warning.png").scaled(20, 20, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        icon.setFixedSize(20, 20)

        title_label = QLabel(title)
        title_label.setStyleSheet("color: white; font-weight: bold;")
        title_label.setAlignment(Qt.AlignVCenter)

        close_btn = QPushButton("✕")
        close_btn.setFixedSize(30, 30)
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: white;
                font-size: 16px;
                border: none;
            }
            QPushButton:hover {
                background-color: #ff5555;
            }
        """)
        close_btn.clicked.connect(self.close)

        top_bar_layout.addWidget(icon)
        top_bar_layout.addWidget(title_label)
        top_bar_layout.addStretch()
        top_bar_layout.addWidget(close_btn)
        top_bar.setLayout(top_bar_layout)
        top_bar.mousePressEvent = self.mousePressEvent
        top_bar.mouseMoveEvent = self.mouseMoveEvent

        main_layout.addWidget(top_bar)

        content_layout = QHBoxLayout()
        content_layout.setContentsMargins(15, 15, 15, 15)
        content_layout.setSpacing(15)

        self.sidebar = QFrame()
        self.sidebar.setObjectName("Sidebar")
        sidebar_layout = QVBoxLayout()
        sidebar_layout.setContentsMargins(5, 5, 5, 5)
        sidebar_layout.setSpacing(10)

        self.isolate_btn = QPushButton("Изоляция устройства")
        self.isolate_btn.setStyleSheet(DARK_BUTTON_STYLE)
        self.check_security_btn = QPushButton("Проверка безопасности")
        self.check_security_btn.setStyleSheet(DARK_BUTTON_STYLE)
        self.ignore_btn = QPushButton("Игнорировать")
        self.ignore_btn.setStyleSheet(DARK_BUTTON_STYLE)
        self.download_btn = QPushButton("Выгрузить массив запросов")
        self.download_btn.setStyleSheet(DARK_BUTTON_STYLE)
        self.delete_btn = QPushButton("Удалить уведомление")
        self.delete_btn.setStyleSheet(DARK_BUTTON_STYLE)

        sidebar_layout.addWidget(self.isolate_btn)
        sidebar_layout.addWidget(self.check_security_btn)
        sidebar_layout.addWidget(self.ignore_btn)
        sidebar_layout.addWidget(self.download_btn)
        sidebar_layout.addWidget(self.delete_btn)

        self.sidebar.setLayout(sidebar_layout)
        content_layout.addWidget(self.sidebar)

        self.details = QFrame()
        details_layout = QVBoxLayout()
        details_layout.setContentsMargins(15, 15, 15, 15)

        created_at_dt = QDateTime.fromString(created_at, Qt.ISODate)
        self.time_label = QLabel(created_at_dt.toString("dd:MM:yyyy hh:mm:ss"))
        self.ip_label = QLabel(f"IP-адрес устройства: {ip}")
        self.extra_info_label = QTextEdit(extra)
        self.extra_info_label.setReadOnly(True)
        self.extra_info_label.setWordWrapMode(QTextOption.WrapAtWordBoundaryOrAnywhere)

        details_layout.addWidget(self.time_label)
        details_layout.addWidget(self.ip_label)
        details_layout.addWidget(self.extra_info_label)

        self.details.setLayout(details_layout)
        content_layout.addWidget(self.details)

        main_layout.addLayout(content_layout)
        self.setFixedSize(600, 420)

        self.isolate_btn.clicked.connect(self.handle_isolate_device)
        self.check_security_btn.clicked.connect(self.handle_check_security)
        self.ignore_btn.clicked.connect(self.handle_ignore)
        self.download_btn.clicked.connect(self.handle_download)
        self.delete_btn.clicked.connect(lambda: self.handle_delete(title))
        self.delete_btn.clicked.connect(self.close)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self.drag_position and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_position)
            event.accept()

    def handle_isolate_device(self):
        print("Изоляция устройства")

    def handle_check_security(self):
        print("Проверка безопасности")

    def handle_ignore(self):
        self.close()

    def handle_download(self):
        print("Выгрузка массива запросов")

    def handle_delete(self, title):
        delete_notification_by_title(title)
        self.notification_deleted.emit(title)
