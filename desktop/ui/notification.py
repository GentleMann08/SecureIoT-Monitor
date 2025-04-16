from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel, QSizePolicy
from PyQt5.QtCore import Qt, QDateTime, QTimer
from ui.notification_details import NotificationDetailsWindow

class NotificationBlock(QFrame):
    def __init__(self, title, ip_address=None, extra=None, created_at=None):
        super().__init__()
        self.setStyleSheet("background-color: white; border: 1px solid #ccc; border-radius: 6px;")
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 8, 10, 6)
        layout.setSpacing(4)

        self.title_label = QLabel(title)
        self.title_label.setStyleSheet("font-size: 13px; font-weight: bold; color: #222; border: none;")
        self.title_label.setWordWrap(True)
        self.title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        layout.addWidget(self.title_label)

        self.time_label = QLabel("")
        self.time_label.setStyleSheet("font-size: 10px; color: #888; margin-top: 4px;")
        layout.addWidget(self.time_label, alignment=Qt.AlignLeft)

        self.setLayout(layout)
        self.setMaximumWidth(480)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)

        self.title = title
        self.ip_address = ip_address
        self.extra = extra
        self.created_at = created_at

        self.mousePressEvent = self.on_click

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        if self.created_at:
            created_at = QDateTime.fromString(self.created_at, Qt.ISODate)
            current_time = QDateTime.currentDateTime()
            time_diff = created_at.secsTo(current_time)
            if time_diff < 60:
                self.time_label.setText(f"{time_diff} секунд назад")
            else:
                self.time_label.setText(f"{time_diff // 60} минут назад")

    def on_click(self, event):
        details_window = NotificationDetailsWindow(self.title, self.time_label.text(), self.ip_address, self.extra)
        details_window.exec_()