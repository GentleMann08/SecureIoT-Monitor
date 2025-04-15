from PyQt5.QtWidgets import QFrame, QVBoxLayout, QPushButton


class Sidebar(QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("Sidebar")
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 20, 10, 10)
        layout.setSpacing(15)

        for item in ["Аккаунт", "Зафиксированные атаки", "Кластеры и паттерны", "Устройства"]:
            button = QPushButton(item)
            button.setFixedHeight(30)
            button.setStyleSheet(
                "QPushButton { text-align: left; padding-left: 10px; font-weight: bold; color: white; background-color: transparent; border: none; }"
                "QPushButton:hover { background-color: #5a5a5a; }"
            )
            layout.addWidget(button)

        layout.addStretch()
        self.setLayout(layout)
        self.setFixedWidth(220)
