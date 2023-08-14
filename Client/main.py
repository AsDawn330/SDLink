import sys
import os

from sdlink_mainwindow import*
import UI.ButtonResource_rc

from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = sdlink_mainwindow()
    w.show()
    sys.exit(app.exec_)
