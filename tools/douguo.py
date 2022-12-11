import requests
import cchardet
url="http://api.douguo.net/recipe/flatcatalogs"
data={
    "client":4,
    "session":1660463690335869169023669776,
    "v":1660462962,
    "_vs":2305
}
headers={
    "client":"4",
    "version":"6922.2",
    "device":"DLT-A0",
    "sdk":"25,7.1.2",
    "imei":"869169023669776",
    "channel":"zhuzhan",
    "mac":"02:00:00:00:00:00",
    "resolution":"1600*900",
    "dpi":"1.5",
    "android-id":"bf9670ade886d913",
    "pseudo-id":"00e0c753",
    "brand":"blackshark",
    "scale":"1.5",
    "timezone":"28800",
    "language":"zh",
    "cns":"0",
    "carrier":"China+Mobile+GSM",
    "imsi":"460009644823396",
    "user-agent":"Mozilla/5.0 (Linux; Android 7.1.2; DLT-A0 Build/N2G48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Safari/537.36",
    "reach":"1",
    "newbie":"1",
    "Content-Type":"application/x-www-form-urlencoded; charset=utf-8",
    "Accept-Encoding":"gzip, deflate",
    "Cookie":"duid=70254628",
    "Host":"api.douguo.net",
    "Content-Length":"68",
    "Connection":"close"

}
response=requests.post(url=url,data=data,headers=headers)

print(response.content.decode("unicode-escape"))