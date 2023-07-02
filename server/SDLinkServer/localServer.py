import os,signal
import sys
import threading
import subprocess

class local_http_server():
    def __init__(self,port,localpath):
        self.Port = port
        self.LocalPath = localpath
        self.Proc = None

    def http_server(self):
        os.chdir(self.LocalPath)
        p = subprocess.Popen('httpd -k start')
        self.Proc = p

    def start_http_server(self):
        self.ServerThread = threading.Thread(target=self.http_server)
        self.ServerThread.start()

    def close(self):
        if(self.Proc):
            self.Proc.terminate()
            self.Proc = None
        result = os.popen('netstat -aon|findstr "' + str(self.Port) + '"')
        portlist = []
        for line in result:
            temp = [i for i in line.split(' ') if i != '']
            if(len(temp)>4):
                port = temp[4].replace('\n','')
                if(not port in portlist):
                    portlist.append(port)
        for port in portlist:
            os.popen('taskkill -f -pid ' + str(port) + ' -t')


if __name__ == '__main__':
    s = local_http_server(9652,'E:\\SDLink')
    s.close()


