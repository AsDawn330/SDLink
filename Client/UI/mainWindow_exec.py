import sys
import os

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from UI.MainWindow import Ui_MainWindow_SDLink
import UI.ButtonResource_rc


class mainWindow_SDLink(QMainWindow,Ui_MainWindow_SDLink):

#Init Function
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setup_ui()

    def setup_ui(self):
        #Window
        self.pushButton_Close.clicked.connect(self.close)
        #Home Page
        self.HomePageWidget = []
        self.HomePageWidget.append(self.label_Home_SDLink)
        self.pushButton_HomePage.clicked.connect(self.SwitchMainState_HomePage)
        #User Interface
        self.UserInterfaceWidget = []
        self.pushButton_UserInterface.clicked.connect(self.SwitchMainState_UserInterface)
        #Library
        self.LibraryWidget = []
        self.pushButton_Library.clicked.connect(self.SwitchMainState_Library)
        #Settings
        self.SettingsWidget = []
        self.pushButton_Settings.clicked.connect(self.SwitchMainState_Settings)

#Home Page Function
    def SwitchMainState_HomePage(self):
        for ui in self.UserInterfaceWidget:
            ui.hide()
        for ui in self.LibraryWidget:
            ui.hide()
        for ui in self.SettingsWidget:
            ui.hide()
        for ui in self.HomePageWidget:
            ui.show()

    def SwitchMainState_UserInterface(self):
        for ui in self.UserInterfaceWidget:
            ui.show()
        for ui in self.LibraryWidget:
            ui.hide()
        for ui in self.SettingsWidget:
            ui.hide()
        for ui in self.HomePageWidget:
            ui.hide()

    def SwitchMainState_Library(self):
        for ui in self.UserInterfaceWidget:
            ui.hide()
        for ui in self.LibraryWidget:
            ui.show()
        for ui in self.SettingsWidget:
            ui.hide()
        for ui in self.HomePageWidget:
            ui.hide()

    def SwitchMainState_Settings(self):
        for ui in self.UserInterfaceWidget:
            ui.hide()
        for ui in self.LibraryWidget:
            ui.hide()
        for ui in self.SettingsWidget:
            ui.show()
        for ui in self.HomePageWidget:
            ui.hide()
#Override Function
    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        if self._tracking:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._startPos = QPoint(e.x(), e.y())
            self._tracking = True

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._tracking = False
            self._startPos = None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = mainWindow_SDLink()
    w.show()
    sys.exit(app.exec_())



