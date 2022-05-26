import requests
import threading
import numpy as np
from redis import StrictRedis
import pymongo
import urllib3
from urllib3.exceptions import InsecureRequestWarning
#########mongo部分#########################
DATABASE_IP = '127.0.0.1'
DATABASE_PORT = 27017
DATABASE_NAME = 'sun'
client = pymongo.MongoClient(DATABASE_IP,DATABASE_PORT)

db = client.sun

# db.authenticate("dba", "dba")
collection = db.px500  # 准备插入数据
urllib3.disable_warnings(InsecureRequestWarning)
########mongo部分#########################

#########redis部分#########################
redis = StrictRedis(host="localhost",port=6379,db=1,decode_responses=True)
#########redis部分#########################

# proxies = { "http": "http://" + ip,
#             "https": "http://" + ip}
#########全局参数部分#########################
START_URL = "https://500px.me/community/v2/user/indexInfo?queriedUserId={}" # 入口链接
COMMENT = "https://500px.me/community/res/relation/{}/follow?startTime=&page={}&size=100&type=json"
HEADERS = {
    "Accept":"application/json",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "X-Requested-With":"XMLHttpRequest"
}

need_crawlids = []  # 待爬取的userid

lock = threading.Lock() # 线程锁
#########全局参数部分#########################

def get_followee():
    try:
        res = requests.get(START_URL.format("5769e51a04209a9b9b6a8c1e656ff9566"),
                           headers=HEADERS,timeout=(5,5),verify=False)
        data = res.json()
        if data:
            totle = int(data["data"]["userFolloweeCount"])  # 返回关注数
            userid = data["data"]["id"]	# 返回用户ID

            return {
                "userid":userid,
                "totle":totle
            }  # 返回总数据
    except Exception as e:
        print("数据获取错误")
        print(e)
if __name__ == '__main__':
    start = get_followee()  # 获取入口
    need_crawlids.append(start)

class Product(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._headers = HEADERS

    def get_follows(self,userid,totle):
        try:
            res = requests.get(COMMENT.format(userid,totle),headers=HEADERS,timeout=(5,5))
            data = res.json()

            if data:
                for item in data:
                    yield {
                        "userid":item["id"],
                        "totle":item["userFolloweeCount"]
                    }
        except Exception as e:
            print("错误信息")
            print(e)
            self.get_follows(userid,totle)  # 出错之后，重新调用

    def run(self):

        while 1:
            global need_crawlids  # 调用全局等待爬取的内容

            if lock.acquire():
                if len(need_crawlids)==0:  # 如果为0，无法进入循环
                    continue

                data = need_crawlids[0]  # 取得第一个
                del need_crawlids[0]  # 使用完删除

                lock.release()

            if data["totle"] == 0:
                continue

            for page in range(1,data["totle"]//100+2):
                for i in self.get_follows(data["userid"],page):
                    if lock.acquire():
                        need_crawlids.append(i)  # 新获取到的，追加到等待爬取的列表里面
                        lock.release()
                    self.save_redis(i)  # 存储到redis里面


    def save_redis(self,data):
        redis.setnx(data["userid"],data["totle"])
        #print(data,"插入成功")

class Consumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while 1:
            key = redis.randomkey() # 随机获取一个key
            if key:
                # 删除获取到的key
                redis.delete(key)
                self.get_info(key)



    def get_info(self,key):
        try:
            res = requests.get(START_URL.format(key),headers=HEADERS,timeout=5)
            data = res.json()
            if data['status'] == "200":
                collection.insert_one(data["data"])  # 插入到mongodb中
        except Exception as e:
            print(e)
            return
if __name__ == '__main__':
    start = get_followee()  # 获取入口
    need_crawlids.append(start)


    p = Product()
    p.start()

    for i in range(1,5):
        c = Consumer()
        c.start()

