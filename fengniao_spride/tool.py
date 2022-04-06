import requests
from retrying import retry
import random
import datetime

class R:
    # 类的初始化方法
    def __init__(self,method="get",params=None,headers=None,cookies=None):
        self.__method = method
        myheaders = self.get_headers()
        if headers is not None:
            myheaders.update(headers)
        self.__headers = myheaders
        self.__cookies = cookies
        self.__params = params

    def get_headers(self):
        print("a")

    @retry(stop_max_attempt_number=3)
    def __retrying_requests(self,url):
        print("a")

    def get_content(self,url,charset="utf-8"):
        try:
            html_str = self.__retrying_requests(url).decode(charset)
        except:
            html_str = None
        return html_str

    def get_file(self,file_url):
        try:
            file = self.__retrying_requests(file_url)
        except:
            file = None
        return file