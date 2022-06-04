import csv
import os
import re
import warnings
import random
import pandas as pd
import requests
import json
from anjuke_spride.getProxies import proxyIp
from fake_useragent import UserAgent
from scrapy import Selector

# useragent = UserAgent()
# headers = {
#     'User-Agent': useragent.random,
# }
#
# proxy_list=list(proxyIp(1))
#
# proxies = {
#     "http"  : proxy_list[0],
#     "https"  : proxy_list[0],
# }
def get_number(pagenum,proxy_list):
    print("开始")
    pageNum2=pagenum
    while pageNum2<100:
        try:
            url="https://m.anjuke.com/aks/tycoon/?ajax=1&p={}".format(pageNum2)
            response=getResponse(url,proxy_list)
            print("第"+str(pageNum2)+"次"+str(response.status_code))

            json_data=json.loads(response.text)
            if json_data['data'] is None:
                print("没有了")
                break
            # else:
            #     print("还有")
            pageNum2+=1
            for i in json_data['data']:
                print("名字："+str(i["broker_name"])+"电话："+str(i["broker_mobile"]))

        except Exception as e:
            proxy_list=list(proxyIp(1))
            print(e)
            print("pagenum"+str(pageNum2))
            get_number(pageNum2,proxy_list)


# jjr_url_list=ssl.xpath("//div[@class=mainlist]").extract()
# print(jjr_url_list)
# print(response.text)
# if __name__ == '__main__':
#     get_number()
def getResponse(url,proxy_list):
    useragent = UserAgent()
    headers = {
        'User-Agent': useragent.random,
    }
    # proxy_list=list(proxyIp(1))
    proxies = {
        "http"  : proxy_list[0],
        "https"  : proxy_list[0],
}
    print(url)
    response=requests.get(url,headers=headers,proxies=proxies)
    return response
if __name__ == '__main__':
    proxy_list=list(proxyIp(2))
    get_number(1,proxy_list)
