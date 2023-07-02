import os
import sys
import yaml
import time
projectPath = os.getcwd().replace('\\QT','')
sys.path.append(projectPath)
from QT.UI.ServerWindow import *
from natApp import *
from localServer import *

class custom_window(QtWidgets.QMainWindow):
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        os.close()

class sdlink_server_window(Ui_MainWindow_SDLink_Server):
    def __init__(self,QMainwindow):
        self.setupUi(QMainwindow)
        self.Name = 'SDLink Server Window'
        t = time.localtime()
        self.logpath = projectPath + '\\Log\\SDLinkServerLog_' + str(t.tm_year) + '_' + str(t.tm_mon) + '_' + str(t.tm_mday) + '_' + str(t.tm_hour) + '_' + str(t.tm_min) + '_' + str(t.tm_sec) + '.txt'
    def setupUi(self, MainWindow_SDLink_Server):
        super().setupUi(MainWindow_SDLink_Server)
        serverConfig = self.load_config()
        if ('LocalPort' in serverConfig):
            self.LocalPort = serverConfig['LocalPort']
            self.lineEdit_Port.setText(str(self.LocalPort))
        if ('HttpdPath' in serverConfig):
            self.HttpdPath = serverConfig['HttpdPath']
            self.lineEdit_HttpdPath.setText(str(self.HttpdPath))
        if ('NatAppPath' in serverConfig):
            self.NatAppPath = serverConfig['NatAppPath']
            self.lineEdit_NatAppPath.setText(str(self.NatAppPath))

        self.pushButton_ChangeHttpdPath.clicked.connect(self.pushbutton_change_httpdPath_clicked)
        self.pushButton_ChangeNatAppPath.clicked.connect(self.pushbutton_change_natapppath_clicked)
        self.pushButton_LocalStart.clicked.connect(self.pushbutton_start_local_clicked)
        self.pushButton_NatAppStart.clicked.connect(self.pushbutton_start_natapp_clicked)
        self.pushButton_ServerStart.clicked.connect(self.pushbutton_start_server_clicked)
        self.pushButton_CloseAll.clicked.connect(self.pushbutton_close_all_clicked)
        self.pushButton_RestartServer.clicked.connect(self.pushbutton_restart_all_clicked)

    def setup_server(self):
        port = self.lineEdit_Port.text()
        httpdPath = self.lineEdit_HttpdPath.text()
        natapppath = self.lineEdit_NatAppPath.text()
        if(not hasattr(self,'LocalServer')):
            self.LocalServer = local_http_server(port,httpdPath)
        if(not hasattr(self,'NatAppControl')):
            self.NatAppControl = natapp_control(natapppath)
        self.LocalPort = port
        self.LocalServer.Port = port
        self.LocalServer.LocalPath = httpdPath
        self.NatAppControl.NatAppPath = natapppath

    def load_config(self):
        ymlpath = projectPath + '\\QT\\serverConfig.yml'
        f = open(ymlpath, 'r')
        Config = yaml.load(f.read(), Loader=yaml.FullLoader)
        return Config
    def save_config(self,config):
        ymlpath = projectPath + '\\QT\\serverConfig.yml'
        f = open(ymlpath, 'w')
        yaml.dump(data=config, stream=f, allow_unicode=True)

    def log(self,msg):
        print(msg)
        t = time.localtime()
        timeset = '[' + str(t.tm_hour) + ':' + str(t.tm_min) + ':' + str(t.tm_sec) + '] '
        text = timeset + msg
        with open(self.logpath,'a') as f:
            f.write(text + '\r\n')
        self.print_to_output(text)
    def print_to_output(self,line):
        self.textBrowser_output.append('<h1>' + line + '</h1>')

    def pushbutton_change_httpdPath_clicked(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(None, "getExistingDirectory", "./")
        config = self.load_config()
        config['HttpdPath'] = path
        self.save_config(config)
        self.lineEdit_HttpdPath.setText(path)
        self.log('Change Html Root Path To : ' + path)
    def pushbutton_change_natapppath_clicked(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(None, "getExistingDirectory", "./")
        config = self.load_config()
        config['NatAppPath'] = path
        self.save_config(config)
        self.lineEdit_NatAppPath.setText(path)
        self.log('Change NatAppPath To : ' + path)
    def pushbutton_start_local_clicked(self):
        self.setup_server()
        self.LocalServer.start_http_server()
        self.log('Start Local Server..(Port : ' + str(self.LocalPort) + ')')
    def pushbutton_start_natapp_clicked(self):
        self.setup_server()
        self.NatAppControl.start_natapp_online()
        self.log('Start NatApp..(DN : ' + self.NatAppControl.DN + ')')
    def pushbutton_start_server_clicked(self):
        self.setup_server()
        self.LocalServer.start_http_server()
        self.NatAppControl.start_natapp_online()
        self.log('Start Server..( Port : ' + str(self.LocalPort) + '  DN : ' + self.NatAppControl.DN + ')')
    def pushbutton_close_all_clicked(self):
        self.LocalServer.close()
        self.NatAppControl.close()
        self.log('Close All..')
    def pushbutton_restart_all_clicked(self):
        self.NatAppControl.close()
        self.LocalServer.close()
        self.setup_server()
        self.LocalServer.start_http_server()
        self.NatAppControl.start_natapp_online()
        self.log('Retart Server..( Port : ' + str(self.LocalPort) + '  DN : ' + self.NatAppControl.DN + ')')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindows = custom_window()
    ui = sdlink_server_window(MainWindows)
    ui.setupUi(MainWindows)
    MainWindows.show()
    sys.exit(app.exec_())
