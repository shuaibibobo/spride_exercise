import csv,os,re,warnings,requests,json,pandas
import random,time
import pandas as pd
from anjuke_spride.getProxies import proxyIp
from fake_useragent import UserAgent
from scrapy import Selector

useragent = UserAgent()
headers = {
    'User-Agent': useragent.random,
}

proxy_list=list(proxyIp(5))

proxies = {
    "http"  : proxy_list[0],
    "https"  : proxy_list[0],
}
def get_city_url():
    url="https://m.anjuke.com/cityList/"
    response=requests.get(url,headers=headers,proxies=proxies)
    print(proxies)
    ssl=Selector(text=response.text)
    city_name=ssl.xpath("//ul[@class='cl-c-l-ul']/li/a/text()")[9:].extract()
    city_url=ssl.xpath("//ul[@class='cl-c-l-ul']/li/a/@href")[9:].extract()
    # city_name=ssl.xpath("//ul[@class='cl-c-l-ul']")[2:].extract()
    # ret = re.search(r'"http:"*".com"',city_name)
    print(city_name)


def get_realtor_info():
    data=pd.read_csv('./csv/address.csv',encoding="utf-8")
    proxy_id=0
    city_dict={}
    city_value=[]
    response=""
    proxies=proxy_list[proxy_id]
    print(proxy_list)
    requests.DEFAULT_RETRIES = 5
    for index in data['城市'].index:
        city_dict[data['城市'].at[index]] = data['地址'].at[index]
    for i,(k,v) in enumerate(city_dict.items()):

        for inum in range(1,3):
            time.sleep(3)
            print("第"+str(inum)+"次")
            url= url="{}tycoon/?ajax=1&p={}".format(v,inum)
            print(url)
            try:
                response=requests.get(url,headers=headers,proxies=proxies)

                if response.content != None:
                    json_data=json.loads(response.text)
                    for i in json_data['data']:
                        print("名字："+str(i["broker_name"])+"电话："+str(i["broker_mobile"]))
                else:
                    print(response.text)

            except Exception as e:
                proxy_id+=1
                proxies = {
                    "http"  : proxy_list[proxy_id],
                    "https"  : proxy_list[proxy_id],
                }
                print(proxies)
                response=requests.get(url,headers=headers,proxies=proxies)
                if response.content != None:
                    json_data=json.loads(response.text)
                    for i in json_data['data']:
                        print("名字："+str(i["broker_name"])+"电话："+str(i["broker_mobile"]))
                else:
                    print(response.text)
            # if i==4:
            #     break
if __name__ == '__main__':
    # proxy_list=random.choice(proxy_lists)
    # proxy_list=list(proxyIp(1))
    # print("ip1"+str(proxy_list))
    # get_number(1,proxy_list)
    get_realtor_info()

