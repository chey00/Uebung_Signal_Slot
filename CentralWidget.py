from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget, QPushButton, QLineEdit, QTextBrowser, QGridLayout


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.__result = 0

        button_add = QPushButton("+")
        button_sub = QPushButton("-")

        button_add.released.connect(self.add_value)
        button_sub.released.connect(self.sub_value)

        self.__value = QLineEdit()

        self.__browser = QTextBrowser()

        grid_layout = QGridLayout()

        grid_layout.addWidget(button_add, 1, 1)
        grid_layout.addWidget(self.__value, 1, 2)
        grid_layout.addWidget(button_sub, 1, 3)
        grid_layout.addWidget(self.__browser, 2, 1, 1, 3)

        self.setLayout(grid_layout)

    @pyqtSlot()
    def add_value(self):
        string = str(self.__result)
        string += " + "

        text = self.__value.text()
        string += text
        string += " = "

        self.__result += int(text)
        string += str(self.__result)

        self.__browser.append(string)

    @pyqtSlot()
    def sub_value(self):
        string = str(self.__result)
        string += " - "

        text = self.__value.text()
        string += text
        string += " = "

        self.__result -= int(text)
        string += str(self.__result)

        self.__browser.append(string)
