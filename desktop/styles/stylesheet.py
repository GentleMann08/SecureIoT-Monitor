STYLESHEET = """
    QMainWindow {
        background-color: #f0f2f5;
    }
    QFrame#Header {
        background-color: #2f2f2f;
    }
    QFrame#Sidebar {
        background-color: #3a3a3a;
    }
    QFrame#Content {
        background-color: #f0f2f5;
    }
"""

CUSTOM_SCROLLBAR = """
    QScrollArea {
        border: none;
    }
    QScrollBar:vertical {
        border: none;
        background: #f1f1f1;
        width: 12px;
        border-radius: 6px;
        margin: 0px 0px 0px 0px;
    }
    QScrollBar::handle:vertical {
        background: #888;
        min-height: 20px;
        border-radius: 6px;
    }
    QScrollBar::handle:vertical:hover {
        background: #555;
    }
    QScrollBar::add-line:vertical {
        height: 0px;
    }
    QScrollBar::sub-line:vertical {
        height: 0px;
    }
    QScrollBar:horizontal {
        border: none;
        background: #f1f1f1;
        height: 12px;
        border-radius: 6px;
        margin: 0px 0px 0px 0px;
    }
    QScrollBar::handle:horizontal {
        background: #888;
        min-width: 20px;
        border-radius: 6px;
    }
    QScrollBar::handle:horizontal:hover {
        background: #555;
    }
    QScrollBar::add-line:horizontal {
        width: 0px;
    }
    QScrollBar::sub-line:horizontal {
        width: 0px;
    }
"""

BUTTON_STYLE = """
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
"""

