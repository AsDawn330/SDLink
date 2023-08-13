import sys
import os

from UI.MainWindow import*
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
import UI.ButtonResource_rc

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow =  PyQt5.QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupUI(MainWindow)
    sys.exit(app.exec_)
