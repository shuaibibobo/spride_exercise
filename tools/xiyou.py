import requests

import gzip
heades={"Host":"novel-content.cdn.bcebos.com",
        "Connection":"keep-alive",
        "Pragma":"no-cache",
        "Cache-Control":"no-cache",
        "sec-ch-ua":"Chromium;v=104, Not A;Brand;v=99, Google Chrome;v=104","sec-ch-ua-mobile":"?0",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
        "sec-ch-ua-platform":"Windows","Accept":"*/*",
        "Origin":"https://boxnovel.baidu.com",
        "Sec-Fetch-Site":"cross-site",
        "Sec-Fetch-Mode":"cors",
        "Sec-Fetch-Dest":"empty",
        "Referer":"https://boxnovel.baidu.com/",
        "Accept-Language":"zh-CN,zh;q=0.9",
}
url="https://novel-content.cdn.bcebos.com/6742163425602392204"

response=requests.get(url=url,headers=heades).content
html_doc=response.decode('utf-8','ignore')

print(html_doc)
