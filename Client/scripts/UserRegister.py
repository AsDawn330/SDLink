import sys
import os
import json
import httpRequests
import  WorkRegister

class sd_link_user:
    def __init__(self,url):
        self.HttpR = httpRequests.sd_requests(url)
        self.Models = []

######### For Public#############
    def Refresh_Models(self):
        self.Models = json.loads(self.HttpR.get_sd_models())
        print(self.Models)


if __name__ == '__main__':
    sdlu = sd_link_user('127.0.0.1:7860')
    sdlu.Refresh_Models()