import csv
import os
import re
import warnings
import random
import pandas as pd
import requests
from anjuke_spride.getProxies import proxyIp
from fake_useragent import UserAgent
from scrapy import Selector
import pymongo

ip=""
proxy = "http://%(ip)s" % {
    "ip" : ip
}
useragent = UserAgent()
headers = {
    'User-Agent': useragent.random,
}
class AnJuKe(object):
    def __init__(self):
        self.citi_list_url= 'https://www.anjuke.com/sy-city.html'
        self.citi_dict={}
        self.proxies_list=list(proxyIp(5))
        self.ua=useragent
        self.path='./'


    def get_citi_list(self):
        UserAgent=self.ua

        ip=random.choice(self.proxies_list)
        proxies = {

            "http"  : ip,
            "https"  : ip,
        }

        response=requests.get(self.citi_list_url,headers=headers,proxies=proxies.__format__(ip),timeout=(5,5))
        sel=Selector(text=response.text)
        # city_name=sel.xpath("//div[@class='city_list']/a/text()").extract()
        city_name = sel.xpath("//div[@class='city_list']/a/text()").extract()
        city_url=sel.xpath("//div[@class='city_list']/a/@href").extract()
        print(city_name)
        # for i in range(len(city_name)):
        #     L=[city_name[i],city_url[i]]
        #     with open('地址表.csv', 'a+',newline='',encoding='gbk') as f:
        #         writer=csv.writer(f)
        #         writer.writerow(L)
        # print("全国地址表打印完成")

    def get_agent_list(self,city,city_url,start_page,end_page):
        for page_num in range(start_page,end_page):
            print("正在打印第{}页经纪人信息".format(page_num))
            UserAgent=self.ua
            agent_url=(city_url+'/tycoon/').format(str(page_num))
            header=headers
            ip=random.choice(self.proxies_list)
            proxies = {
                "http"  : ip,
                "https"  : ip,
            }
            request_count=0
            while request_count<5:
                try:
                    response=requests.get(agent_url,headers=headers,proxies=proxies,timeout=5)
                    if(response.status_code == 200) and ('访问验证' not in response.text):
                        ip=random.choice(self.proxies_list)
                        proxies = {
                            "http"  : ip,
                            "https"  : ip,
                        }
                        response=requests.get(agent_url,headers=headers,proxies=proxies,timeout=5)
                        request_count += 1
                    else:
                        ip=random.choice(self.proxies_list)
                        proxies = {
                            "http"  : ip,
                            "https"  : ip,
                        }
                        response=requests.get(agent_url,headers=headers,proxies=proxies,timeout=5)
                        request_count += 1
                except Exception as e:
                    request_count+=1
                    print(e)
            ssl=Selector(text=response.text)
            jjr_url_list=ssl.xpath("//div[@class=mainlist/div/a/@href]").extract
            print(jjr_url_list)


















if __name__ == '__main__':
    ajk = AnJuKe()
    ajk.get_agent_list(city="cirt",city_url="https://akesu.anjuke.com/",start_page=1,end_page=2)

