from PyQt5.QtWidgets import QFrame, QHBoxLayout, QPushButton


class WindowControls(QFrame):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

        self.min_btn = QPushButton("-")
        self.max_btn = QPushButton("□")
        self.close_btn = QPushButton("x")

        for btn in [self.min_btn, self.max_btn, self.close_btn]:
            btn.setFixedSize(20, 20)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #555;
                    color: white;
                    border: none;
                    border-radius: 2px;
                }
                QPushButton:hover {
                    background-color: #777;
                }
            """)
            layout.addWidget(btn)

        self.min_btn.clicked.connect(self.main_window.showMinimized)
        self.max_btn.clicked.connect(self.toggle_max_restore)
        self.close_btn.clicked.connect(self.main_window.close)

        self.setLayout(layout)

    def toggle_max_restore(self):
        if self.main_window.isMaximized():
            self.main_window.showNormal()
        else:
            self.main_window.showMaximized()
