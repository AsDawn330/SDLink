import sys
import os
import eel

@eel.expose
def read_filelist(path):
    files = os.listdir(path)
    return files

eel.init('E:\SDLink\server\html')
eel.start('index.html',port=7860)