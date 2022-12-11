import requests
from fake_useragent import UserAgent
import json
useragent = UserAgent()
headers = {
    'User-Agent': useragent.random,
}

def get_proxy(count):
    count=2

    proxies_url="http://xcy004c347091075.user.xiecaiyun.com/api/proxies?action=getJSON&key=NP90A4743E&count={}&word=&rand=true&norepeat=true&detail=false&ltime=0"
    url=proxies_url.format(count)
    resposne=requests.get(url)
    proxy_josn=json.loads(resposne.text)

    for i in proxy_josn['result']:
        print(str(i['ip'])+":"+str(i['port']))
        ip=str(i['ip'])+":"+str(i['port'])
        yield ip
get_proxy(2)
