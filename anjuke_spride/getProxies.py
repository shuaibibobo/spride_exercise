import requests,json,random
from fake_useragent import UserAgent
def proxyIp(quantity):

    ip="https://h.shanchendaili.com/api.html?action=get_ip&key=HUae23a44b0526153754Ok6C&time=10&count={}&protocol=http&type=json&only=0"
    test=requests.get(ip.format(quantity))
    # proxy_josn=json.loads(test.text)
    # proxy=proxy_josn["list"][0]
    # print(str(proxy['sever'])+":"+str(proxy["port"]))
    proxy_josn=json.loads(test.text)
    # print(proxy_josn)
    proxy=proxy_josn["list"]
    ips=[]
    for i in proxy:
        # print(str(i['sever'])+":"+str(i["port"]))
        ip=str(i['sever'])+":"+str(i["port"])
        yield ip

#
# ips=list(proxyIp(1))
# print(ips[0])
# for i in ips:
#     print(i)


# ip=ips[0]
# print(ip)
# for i in ip:
#     print(i)
# ip=random.choice(ips)
# print("random"+str(ip))
# proxy = "http://%(ip)s" % {
#     "ip" : ip
# }
# proxies = {
#
#     "http"  : proxy,
#     "https"  : proxy,
# }
# url="http://httpbin.org/ip"
# useragent = UserAgent()
# headers = {
#     'User-Agent': useragent.random,
# }
# response=requests.get(url,headers=headers,proxies=proxies,timeout=5)
# html = response.text
# print(html)