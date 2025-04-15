from PyQt5.QtWidgets import QFrame, QHBoxLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt


class SearchBlock(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #2e2e2e;")
        layout = QHBoxLayout()
        layout.setContentsMargins(10, 12, 10, 12)
        layout.setSpacing(10)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Найти тег, устройство или уязвимость")
        self.search_input.setStyleSheet(
            "background-color: #3a3a3a; color: white; border: none; border-radius: 5px; padding: 6px 10px;"
        )
        self.search_input.setFixedHeight(30)
        layout.addWidget(self.search_input)

        self.prevent_btn = QPushButton("Профилактика")
        self.prevent_btn.setFixedHeight(30)
        self.prevent_btn.setStyleSheet(
            "QPushButton { background-color: #4caf50; color: white; padding: 4px 15px; border-radius: 5px; }"
            "QPushButton:hover { background-color: #45a049; }"
        )
        layout.addWidget(self.prevent_btn)

        self.setLayout(layout)
        self.setFixedHeight(64)
