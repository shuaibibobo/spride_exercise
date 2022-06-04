import requests


url="https://api.yglz.hebnews.cn/api/system/homePage/getMessageList"
data={"pageNum":2,"pageSize":10,"type":2}
response = requests.post(url, json=data)
# 获取响应状态码
print('状态码：', response.status_code)
# 获取响应头
print('响应头信息：', response.headers)
# 获取响应正文
print('响应正文：', response.text)
class test():
    def __init__(self):
        self.proxy_list={1241}
    def getaleen(self):
        self.proxy_list

