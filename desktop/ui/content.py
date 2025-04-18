from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QScrollArea
from PyQt5.QtCore import Qt, QTimer
from .search_block import SearchBlock
from .notification import NotificationBlock
from database.db import get_notifications, clear_notifications
from styles.stylesheet import CUSTOM_SCROLLBAR, BUTTON_STYLE

class Content(QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("Content")
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 15)
        layout.setSpacing(15)

        self.search_block = SearchBlock()
        layout.addWidget(self.search_block)

        top_controls_layout = QHBoxLayout()
        top_controls_layout.setContentsMargins(30, 0, 30, 0)

        top_controls_layout.addStretch()

        self.clear_btn = QPushButton("Удалить все уведомления")
        self.clear_btn.setFixedHeight(28)
        self.clear_btn.setStyleSheet(BUTTON_STYLE)
        self.clear_btn.clicked.connect(self.clear_notifications)

        top_controls_layout.addWidget(self.clear_btn)
        layout.addLayout(top_controls_layout)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet(CUSTOM_SCROLLBAR)

        self.notifications_widget = QWidget()
        self.notifications_layout = QVBoxLayout()
        self.notifications_layout.setContentsMargins(30, 0, 0, 0)
        self.notifications_layout.setSpacing(10)

        self.notifications_widget.setLayout(self.notifications_layout)
        self.scroll_area.setWidget(self.notifications_widget)

        layout.addWidget(self.scroll_area)

        self.setLayout(layout)
        self.load_notifications()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.load_notifications)
        self.timer.start(10000)

    def load_notifications(self):
        for i in reversed(range(self.notifications_layout.count())):
            self.notifications_layout.itemAt(i).widget().setParent(None)
        for title, time_info, ip, extra, created_at in get_notifications():
            notification_block = NotificationBlock(title, ip, extra, created_at)
            notification_block.notification_deleted.connect(self.remove_notification)
            self.notifications_layout.addWidget(notification_block)

    def remove_notification(self, title):
        for i in reversed(range(self.notifications_layout.count())):
            widget = self.notifications_layout.itemAt(i).widget()
            if isinstance(widget, NotificationBlock) and widget.title == title:
                self.notifications_layout.removeWidget(widget)
                widget.setParent(None)
                break

    def clear_notifications(self):
        clear_notifications()
        self.load_notifications()
