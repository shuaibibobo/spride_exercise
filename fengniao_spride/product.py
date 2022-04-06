from fengniao_spride.http_help import R
import threading
import time
import json
import re

img_list=[]
imgs_lock=threading.Lock()

class product(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.__headers = {"Referer":"http://image.fengniao.com/",
                          "Host": "image.fengniao.com",
                          "X-Requested-With":"XMLHttpRequest"
                          }
        self.__start="https://image.fengniao.com/index.php?action=getList&class_id=192&sub_classid=0&page={}&not_in_id=5361629,5361266,5361068"
        self.__res=R(headers=self.__headers)
    def run(self):
        index=2
        while True:
            url=self.__start.format(index)
            print("开始操作:{}".format(url))
            index+=1
            content=self.__res.get_content(url,charset="gbk")
            if content is None:
                print("可能没有了")
                break
            time.sleep(3)
            json_content=json.load(content)

            if json_content["status"]==1:
                for item in json_content["data"]:
                    title=item["title"]
                    child_url=item["url"]
                    img_content=self.__res.get_content(child_url,charset="gbk")


a=product()
a.run()