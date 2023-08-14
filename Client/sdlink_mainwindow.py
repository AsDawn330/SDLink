import sys
import os

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from UI.MainWindow import *

class sdlink_mainwindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(sdlink_mainwindow, self).__init__()
        self.setup_win()

    def setup_win(self):
        self.setupUi(self)
        self.setWindowTitle('SDLink')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = sdlink_mainwindow()
    w.show()
    sys.exit(app.exec_())