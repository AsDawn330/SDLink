import sys
import os
import requests
import json

class sd_requests:
    def __init__(self,url):
        self.url = url
        if(not self.url.startswith('http:')):
            self.url = 'http://' + self.url
        try:
            requests.get(self.url)
        except:
            print('[Error]: Unable to link to ' + url)

    def get_sd_models(self):
        get_url = self.url + '/sdapi/v1/sd-models'
        try:
            r = requests.get(get_url)
            return r.text
        except:
            print('[Error]: Failed to get sd models from ' + get_url)

    def txt2img(self,settings):
        post_url = self.url + '/sdapi/v1/txt2img'
        try:
            r = requests.post(post_url,data=json.dumps(settings))
            return r.text
        except:
            print('[Error]: Failed to run txt2img in ' + post_url)

if __name__ == '__main__':
    sdr = sd_requests('127.0.0.1:7860')
    modeltxt = sdr.get_sd_models()
