import os
import sys
import json

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
    print(len(testLib['images']))
    for img in testLib['images']:
        print(img)
