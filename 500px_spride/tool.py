import requests,json,sys
from fake_useragent import UserAgent

# def getProxyIp(quantity):
ip="https://h.shanchendaili.com/api.html?action=get_ip&key=HUae23a44b0526153754Ok6C&time=10&count={}&protocol=http&type=json&only=0"
quantity=3
test=requests.get(ip.format(quantity))
    # proxy_josn=json.loads(test.text)
    # proxy=proxy_josn["list"][0]
    # print(str(proxy['sever'])+":"+str(proxy["port"]))
proxy_josn=json.loads(test.text)
print(proxy_josn)
proxy=proxy_josn["list"]
ips=[]
for i in proxy:
    print(str(i['sever'])+":"+str(i["port"]))
    ips.append(str(i['sever'])+":"+str(i["port"]))
# yield ips
# ip=getProxyIp(1)

# for ip in ips:
#     ip_port = ip
#     #ip_port为空时只返回本机ip,为代理ip时返回本机ip和代理ip
#     proxies = {
#         'http': ip_port,
#         'https': ip_port
#     }
#     #ip检测网址
#     # url="http://httpbin.org/ip"
#     url="https://tousu.hebnews.cn/"
#     useragent = UserAgent()
#     headers = {
#         'User-Agent': useragent.random,
#     }
#     if not ip_port:
#         print('ip_port不能为空')
#         sys.exit(0)
#     try:
#         response=requests.get(url,headers=headers,proxies=proxies,timeout=5)
#         print(headers)
#         # if response.status_code==200:
#         #     proxyip.append(ip)
#         print(response.status_code)
#         # proxyip.append(ip)
#         # html = response.text
#         # print(html)
#         # print(response.status_code)
#     except :
#         print("null")


