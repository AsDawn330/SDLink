import os
import sys
import json
import base64

class sd_link_lib:
    def __init__(self,path):
        self.Path = path
        if (not os.path.exists(self.Path)):
            print('[Error]: Lib Path Not Exists')
            return
        self.Refresh_Collections()

    def Refresh_Collections(self):
        self.Collections = []
        listjsons = os.listdir(self.Path)
        for js in listjsons:
            if (js.endswith('.json')):
                self.Collections.append(js)

    def Read_Collection_From_Json(self,jsonname):
        jsonpath = self.Path + '/' + jsonname
        with open(jsonpath,'r') as json_file:
            dict = json.loads(json_file.read())
            return dict

if __name__ == '__main__':
    sdlb = sd_link_lib('E:/tmp')
    testLib = sdlb.Read_Collection_From_Json(sdlb.Collections[0])
    b = str.encode(testLib['images'][0])
    print(type(b))
    imgdata = base64.b64decode(b)
    with open("E:/temp.jpg", 'wb') as f:
        f.write(imgdata)

