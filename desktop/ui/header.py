from PyQt5.QtWidgets import QFrame, QHBoxLayout, QLabel
from widgets.window_controls import WindowControls


class Header(QFrame):
    def __init__(self, main_window):
        super().__init__()
        self.setObjectName("Header")
        layout = QHBoxLayout()
        layout.setContentsMargins(15, 10, 15, 10)
        layout.setSpacing(10)

        title = QLabel("IOT Security Monitor")
        title.setStyleSheet("font-size: 16px; font-weight: bold; color: white; margin-top: 5px;")
        layout.addWidget(title)

        layout.addStretch()
        layout.addWidget(WindowControls(main_window=main_window))
        self.setLayout(layout)
        self.setFixedHeight(60)
