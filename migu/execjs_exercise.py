import execjs
import requests
from lxml import etree
from fake_useragent import UserAgent
with open(r"./migu.js", encoding="utf-8") as f:
    ctx = execjs.compile(f.read())
    fingerprint=ctx.call('getFingerprint')
    getpwd=ctx.call('getPwd','18200370702','@Xcb1314520')
data={
'sourceID':208003,
'appType':0,
'imgcodeType':1,
'rememberMeBox':1,
'loginID':getpwd[0],
'enpassword':getpwd[1],
'fingerPrint':fingerprint["result"],
'fingerprintDetails':fingerprint["details"],
'isAsync':True
}

url="https://passport.migu.cn/authn"
useragent = UserAgent()
headers={
    'User-Agent': useragent.random,
}
response=requests.post(url=url,data=data)
# print(response.text)

url2="https://www.migu.cn/index.html"
print(requests.get(url).text)
# response2=requests.get(url=url2,headers=headers)
# html=etree.HTML(response2.text)
# user_name=html.xpath('/html/body/div[1]/div/div/div[2]/div/div[2]/a')
# print(type(user_name))
# print(user_name[0])
# print(user_name[0].text)

# response2=requests.get("https://www.migu.cn/user/pcuser",headers=headers)
# response2=etree.HTML(response2.text)
# user_name=response2.xpath('/html/body/div[1]/div/div/div[2]/div/div[2]/a/img')
# print(response2.text)

# print(fingerprint["details"])
data={
    
}