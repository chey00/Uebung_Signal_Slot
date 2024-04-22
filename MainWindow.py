from PyQt6.QtWidgets import QMainWindow

from CentralWidget import CentralWidget

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        centralWidget = CentralWidget(self)

        self.setCentralWidget(centralWidget)

        self.setWindowTitle("Taschenrechner")
