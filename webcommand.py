from time import sleep
# import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from __future__ import unicode_literals
from yt_dlp import YoutubeDL

class Web():


    def __init__(self):

        youtube_url = "https://www.youtube.com/"

        self.start(youtube_url)



    def start(self, url=None, disp = False):
        chrome_path = "C:\Path\Chrome\chromedriver.exe"

        options = Options()
        if disp:
            options.add_argument('--headless')

        self.browser = webdriver.Chrome(chrome_path, options = options)
        
        #待機時間
        sleep(2)
        if url != None:
            self.browser.get(url)


    def quit(self):

        self.cur_url = self.browser.current_url
        self.browser.quit()


    def download(self):

        ydl_opts = {'format': 'best'}
        with YoutubeDL(ydl_opts) as ydl:
            result = ydl.download([self.cur_url])
            print(result)

    def test_url(self):
        self.cur_url = "https://www.youtube.com/watch?v=cm-l2h6GB8Q"
