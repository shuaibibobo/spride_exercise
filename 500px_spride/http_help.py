import random
import numpy as np
import requests
import re
from bs4 import BeautifulSoup
file=open("./ip.txt",'r', encoding='UTF-8')

proxies_list=file.readlines()

ip_list = []




url = 'http://icanhazip.com'

#
# # for i in proxies_list:
# #     print(i.replace("\n","").replace("\r", ""))
#
# # print(proxies_list[1].split())
# # print(proxies_list[2].split())
# # str1=re.sub('[\n]+', '\n', proxies_list[1])
# # print(str1)
# ip_list = []
# for proxy_ip in proxies_list:
#     proxy_ip=proxy_ip.replace("\n","").replace("\r", "")
#     print(proxy_ip)
#     # print(proxies_list)
#     proxies = {'http': proxy_ip}
#     try:
#         wb_data = requests.get(url=url,timeout=5,proxies=proxies)
#         flag = True
#     except:
#         # proxies_list.remove(proxies['http'])
#         flag = False
#
#     if flag:
#         ip_list.append(proxies['http'])
# print(ip_list)

import requests
url = 'http://httpbin.org/ip'
proxies_list = [
    'http://117.66.167.116:8118',
    'http://118.190.95.35:9001',
    'http://116.77.204.2:80',
    'http://110.40.13.5:80',
    "112.6.117.135:8085",
    "5.189.140.113:8118",
    "194.233.73.105:443",
    "45.32.10.63:1081",
    "218.75.102.198:8000",
    "106.54.128.253:999"
]
ip_list = []

# for proxy_ip in proxies_list:
#     print (proxy_ip)
#     # print(proxies_list)
#     proxies = {'http': proxy_ip}
#     try:
#         wb_data = requests.get(url=url,proxies=proxies)
#         flag = True
#     except:
#         proxies_list.remove(proxies['http'])
#         flag = False
#
#     if flag:
#         ip_list.append(proxies['http'])
# print (ip_list)


# def jiance(ip_port):
#     ip = ip_port.split(':')[0]
#     proxies = {
#         'http': ip_port,
#         'https': ip_port
#     }
    url="http://httpbin.org/ip"
    header={'User-Agent':'Mozilla/5.0'}
    if not proxies_list:
        print('ip_port不能为空')

    try:
        response=requests.get(url,headers=header,proxies=proxies,timeout=5)
        # print(response)
        html = response.text
        # print(html)
        if ip in html:
            print('ip有效',ip_port)
        # print(html)
        else:
            print('ip无效')
    except :
        print("超时")

#获得的ip数据
# datas = [
#     '54.38.181.125:3128',
#     '218.252.244.104:80',
#     '95.216.12.141:22214',
#     '116.117.134.135:8081',
#     '194.233.73.105:443',
#     '116.117.134.135:9999',
#     '180.97.34.35:80',
#     '202.108.22.5:80',
#     '218.59.139.238:80',
#     '220.181.111.37:80',
#     '222.74.202.232:80',
#     '222.74.202.233:80',
#     '222.74.202.233:9999',
#     '222.74.202.234:8081',
#     '222.74.202.237:80',
#     '222.74.202.238:8080',
#     '222.74.202.239:80',
#     '222.74.202.239:8080',
#     '222.74.202.240:9999',
#     '222.74.202.243:80',
#     '222.74.202.245:80',
#     '47.98.183.59:3128',
# ]
#
# for ip_port in datas:
#     jiance(ip_port)
