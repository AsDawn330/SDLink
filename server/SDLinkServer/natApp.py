import os,signal
import threading
import subprocess
from time import sleep

class natapp_control():
    def __init__(self,natapppath):
        self.NatAppPath = natapppath
        self.LogPath = self.NatAppPath + '\\tmp\\stdout.txt'
        self.DN = ''
        self.Proc = None
    def natapp_online(self):
        os.chdir(self.NatAppPath)
        os.remove(self.LogPath)
        self.Proc = subprocess.Popen('cmd.exe /c start.bat')
    def start_natapp_online(self):
        self.NatAppThread = threading.Thread(target=self.natapp_online)
        self.NatAppThread.start()
        sleep(1)
        self.get_DN()
    def get_log(self):
        if(os.path.exists(self.LogPath)):
            txt = []
            f = open(self.LogPath,'r')
            line = f.readline().strip()
            while(line):
                txt.append(line)
                line = f.readline().strip()
            return txt
        return None

    def get_DN(self):
        DNLog = self.get_log()[3]
        DN = DNLog[DNLog.rfind('established at ') + 15:]
        self.DN = DN

    def close(self):
        if(self.Proc):
            self.Proc.terminate()
            self.Proc = None
            os.system('TASKKILL /F /IM natapp.exe /T')
