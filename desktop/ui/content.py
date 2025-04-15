from PyQt5.QtWidgets import QFrame, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from ui.search_block import SearchBlock
from ui.notification import NotificationBlock
from database.db import get_notifications


class Content(QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("Content")
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 15)
        layout.setSpacing(15)

        self.search_block = SearchBlock()
        layout.addWidget(self.search_block)

        self.notifications_layout = QVBoxLayout()
        self.notifications_layout.setContentsMargins(30, 0, 0, 0)
        self.notifications_layout.setSpacing(10)

        for title, time_info in get_notifications():
            self.notifications_layout.addWidget(NotificationBlock(title, time_info))

        container = QWidget()
        container.setLayout(self.notifications_layout)
        layout.addWidget(container, alignment=Qt.AlignTop)

        self.setLayout(layout)
