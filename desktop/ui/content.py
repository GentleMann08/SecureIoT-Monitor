from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import Qt
from .search_block import SearchBlock
from .notification import NotificationBlock
from database.db import get_notifications, clear_notifications


class Content(QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("Content")
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 15, 15)
        layout.setSpacing(15)

        self.search_block = SearchBlock()
        layout.addWidget(self.search_block)

        top_controls_layout = QHBoxLayout()
        top_controls_layout.setContentsMargins(30, 0, 30, 0)

        top_controls_layout.addStretch()

        self.clear_btn = QPushButton("Удалить все уведомления")
        self.clear_btn.setFixedHeight(28)
        self.clear_btn.setStyleSheet("""
            QPushButton {
                background-color: #e53935;
                color: white;
                padding: 6px 12px;
                border: none;
                border-radius: 6px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #c62828;
            }
        """)
        self.clear_btn.clicked.connect(self.clear_notifications)

        top_controls_layout.addWidget(self.clear_btn)
        layout.addLayout(top_controls_layout)

        self.notifications_layout = QVBoxLayout()
        self.notifications_layout.setContentsMargins(30, 0, 0, 0)
        self.notifications_layout.setSpacing(10)

        self.container = QWidget()
        self.container.setLayout(self.notifications_layout)
        layout.addWidget(self.container, alignment=Qt.AlignTop)

        self.setLayout(layout)
        self.load_notifications()

    def load_notifications(self):
        for i in reversed(range(self.notifications_layout.count())):
            self.notifications_layout.itemAt(i).widget().setParent(None)
        for title, time_info, ip, extra in get_notifications():
            self.notifications_layout.addWidget(
                NotificationBlock(title, time_info, ip, extra)
            )

    def clear_notifications(self):
        clear_notifications()
        self.load_notifications()
