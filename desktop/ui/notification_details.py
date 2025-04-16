from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt


class NotificationDetailsWindow(QDialog):
    def __init__(self, title, time_info, ip_address, extra):
        super().__init__()
        self.setWindowTitle("Детали уведомления")
        self.setFixedSize(480, 300)
        self.setStyleSheet("""
            QDialog {
                background-color: #f9f9f9;
                font-family: Arial;
            }
            QLabel {
                font-size: 14px;
                color: #333;
            }
            QLabel#Header {
                font-size: 16px;
                font-weight: bold;
                margin-bottom: 8px;
            }
            QPushButton {
                background-color: #3a77d2;
                color: white;
                padding: 8px 16px;
                border: none;
                border-radius: 6px;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: #345f9f;
            }
            QPushButton#Ignore {
                background-color: #aaa;
            }
            QPushButton#Ignore:hover {
                background-color: #888;
            }
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)

        header = QLabel("Информация об уведомлении")
        header.setObjectName("Header")
        layout.addWidget(header)

        layout.addWidget(QLabel(f"Заголовок: {title}"))
        layout.addWidget(QLabel(f"Время: {time_info}"))
        layout.addWidget(QLabel(f"IP-адрес: {ip_address or 'Нет данных'}"))
        layout.addWidget(QLabel(f"Дополнительно: {extra or 'Нет данных'}"))

        layout.addStretch()

        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)

        isolate_btn = QPushButton("Изоляция устройства")
        security_btn = QPushButton("Проверка безопасности")
        ignore_btn = QPushButton("Игнорировать")
        ignore_btn.setObjectName("Ignore")

        isolate_btn.clicked.connect(self.isolate_device)
        security_btn.clicked.connect(self.check_security)
        ignore_btn.clicked.connect(self.ignore)

        button_layout.addWidget(isolate_btn)
        button_layout.addWidget(security_btn)
        button_layout.addWidget(ignore_btn)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def isolate_device(self):
        print("Изоляция устройства!")
        self.accept()

    def check_security(self):
        print("Проверка безопасности устройства!")
        self.accept()

    def ignore(self):
        print("Игнорирование уведомления!")
        self.accept()