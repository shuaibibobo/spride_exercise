import requests
from lxml import etree
import json
from fengniao_spride.http_help import R
import threading
import base64
import urllib
from urllib.parse import quote
from bs4 import BeautifulSoup
import time
import random
# response=requests.get("http://ww.baidu.com")
# html=response.content.decode("utf-8")
# tree=etree.HTML(html)
#
# hrefs=tree.xpath('//a')
# for href in hrefs:
#     print(href.get("href"))
#     print(href.text)
# response=requests.get("http://yglz.tousu.hebnews.cn/sssb-1.html")html
# html=response.content.decode("utf-8")
# print(html)

# headers = {"Referer":"http://yglz.tousu.hebnews.cn/",
#            "origin": "http://yglz.tousu.hebnews.cn",
#            "content-type": "application/json",}
# params={"pageNum":"1","pageSize":"500","type":"2"}
#
# url = "https://api.yglz.hebnews.cn/api/system/homePage/getMessageList"
# response = requests.post(url,json=params,headers=headers,timeout=3)
# json_data=json.loads(response.content)
# json_list=[]
#
# for i in json_data["data"]:
#     json_list.append(i["msgId"])
# print(len(json_list))


# id_json=json.load(response.content)
# for i in response:
#     id_json.append(response["msgId"])
#
# print(id_json.count("msgId"))
# url="https://api.yglz.hebnews.cn/api/system/cptMessage/getMessageDetail"
# detail_data={"mhId":"551074","msgId":"L178718"}
# response = requests.post(url,json=detail_data,headers=headers,timeout=3)
# print(response.content.decode("utf-8"))

# headers = {"Referer":"https://stock.tuchong.com/search?availableOnly=&page=4&platform=image&searchFrom=recommendation&search_id=7084130319124660492&size=100&sortBy=0&term={}&topic_id=&utm_source=tuchong_pc_community",
#            "content-type": "application/json"}
# url="https://stock.tuchong.com/api/search/image?page=4&platform=&search_from=recommendation&search_id=7084130319124660492&size=100&sort_by=0&term={}"
# keyword="山川"
#
# headers["Referer"]=headers["Referer"].format(quote(keyword))
# url=url.format(quote("keyword"))
# response=requests.get(url,headers=headers)
# print(response.content.decode("utf-8"))
# f = quote('山川')
# print(urllib.parse.unquote('%E6%B1%89%E5%AD%97'))
#
# print(f)
# f="FQfCBeWWHXy7akes1ggZ+7rz3H3VRcPzLvaMS5VSJYs1teLIh6Fo6zSJiCMLSgtxxFve/CQ/C7zp50C8u9xkyySui7l7EQ8Wt"
# print(urllib.parse.unquote(f))

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
# }
#
# url="http://jandan.net/ooxx/MjAyMjA0MDgtMTc=#comments"
# print(requests.get(url,headers=headers).content.decode("utf-8"))

# def get_html(url):
#
#     resp = requests.get(url = url, headers = headers)
#     soup = BeautifulSoup(resp.text,features="lxml")
#     return soup
#
# def get_next_page(soup):
#     next_page = soup.find(class_='previous-comment-page')
#     next_page_href = next_page.get('href')
#     print(next_page_href)
#     return f'http:{next_page_href}'
# def get_img_url(soup):
#     a_list = soup.find_all(class_ = 'view_img_link')
#     urls = []
#     for a in a_list:
#         href = 'http:' + a.get('href')
#         urls.append(href)
#     return urls
# a=get_html("http://jandan.net/ooxx/MjAyMjA0MDgtMTc=#comments")
# print(a.findAll('img'))

url="https://500px.com.cn/community/v2/user/indexInfo?queriedUserId=cc138308a439c9e6fd61f5826e1c74172"
headers={
    "Referer":"https://500px.com.cn/community/user-details/cc138308a439c9e6fd61f5826e1c74172",
    "Host":"500px.com.cn"
    # "acw_tc":"2760828616494733004055283e838cab91455d91d2ee3e5ce80cbf3cf6e40d"
}
response=requests.get(url,headers=headers)
print(response.content.decode("utf-8"))