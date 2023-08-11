import sys
import os
import json
import time
import httpRequests
import  WorkRegister

class sd_link_user:
    def __init__(self,url,libpath):
        self.HttpR = httpRequests.sd_requests(url)
        self.Models = []
        self.CurrentGenetateSetting = {}
        self.TaskTheme = ''
        self.LibPath = libpath
        if(not os.path.exists(self.LibPath)):
            print('[Error]: Lib Path Not Exists')


######### For Public#############
    def Refresh_Models(self):
        self.Models = json.loads(self.HttpR.get_sd_models())
        print(self.Models)

    def Build_Generate_Setting(self,prompt='',negative_prompt='',seed=-1,batch_size=1,n_iter=1,steps=20,
                               cfg_scale=7,width=512,height=512,restore_faces=False,tiling=False,denoising_strength=0):
        dict = {}
        dict['prompt'] = prompt
        dict['negative_prompt'] = negative_prompt
        dict['seed'] = seed
        dict['bacth_size'] = batch_size
        dict['n_iter'] = n_iter
        dict['steps'] = steps
        dict['cfg_scale'] = cfg_scale
        dict['wdith'] = width
        dict['height'] = height
        dict['restore_faces'] = restore_faces
        dict['tiling'] = tiling
        dict['denoising_strength'] = denoising_strength

        self.CurrentGenetateSetting = dict

        return dict

    def RunTxt2Img(self):
        if(self.CurrentGenetateSetting == {}):
            print('[Error]: No Setting for Running')
        else:
            r = self.HttpR.txt2img(self.CurrentGenetateSetting)
            t = time.localtime()
            jsonpath = self.LibPath + '\\' + self.TaskTheme + '_' + str(t.tm_year) + '_' + str(t.tm_mon) + '_' + str(t.tm_mday) + '_' + str(t.tm_hour) + '_' + str(t.tm_min) + '_' + str(t.tm_sec) + '.json'
            json_str = json.dumps(json.loads(r),indent=4,ensure_ascii=False)
            with open(jsonpath,'w') as json_file:
                json_file.write(json_str)




if __name__ == '__main__':
    sdlu = sd_link_user('127.0.0.1:7860','E:\\tmp')
    sdlu.TaskTheme = 'Test'
    sdlu.Build_Generate_Setting(prompt='1dog wearing clothes')
    sdlu.RunTxt2Img()

