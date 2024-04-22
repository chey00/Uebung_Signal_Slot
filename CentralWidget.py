from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget, QPushButton, QLineEdit, QTextBrowser, QGridLayout


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.result = 0

        button_add = QPushButton("+")
        button_add.released.connect(self.add_value)

        button_sub = QPushButton("-")

        self.line_value = QLineEdit()

        self.browser_result = QTextBrowser()

        grid_layout = QGridLayout()

        grid_layout.addWidget(button_add, 1, 1)
        grid_layout.addWidget(self.line_value, 1, 2)
        grid_layout.addWidget(button_sub, 1, 3)
        grid_layout.addWidget(self.browser_result, 2, 1, 1, 3)

        self.setLayout(grid_layout)

    @pyqtSlot()
    def add_value(self):
        string = str(self.result)
        string += " + "

        text = self.line_value.text()
        string += text
        string += " = "

        self.result += int(text)
        string += str(self.result)

        self.browser_result.append(string)
