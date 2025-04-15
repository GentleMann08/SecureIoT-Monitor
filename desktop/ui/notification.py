from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel, QSizePolicy
from PyQt5.QtCore import Qt


class NotificationBlock(QFrame):
    def __init__(self, title, time_info):
        super().__init__()
        self.setStyleSheet("background-color: white; border: 1px solid #ccc; border-radius: 6px;")
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 8, 10, 6)
        layout.setSpacing(4)

        label = QLabel(title)
        label.setStyleSheet("font-size: 13px; font-weight: bold; color: #222; border: none;")
        label.setWordWrap(True)
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        layout.addWidget(label)

        time_label = QLabel(time_info)
        time_label.setStyleSheet("font-size: 10px; color: #888; margin-top: 4px;")
        layout.addWidget(time_label, alignment=Qt.AlignLeft)

        self.setLayout(layout)
        self.setMaximumWidth(480)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
