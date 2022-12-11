
import datetime
import random
import time
import re
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pymongo
from lxml import etree
import requests
from pyquery import PyQuery as pq
client = pymongo.MongoClient('localhost',27017)
shidai = client['gongyuan']
comments = shidai['comments']
path_one = r'C:\Users\aleen\AppData\Local\Programs\Python\Python37\chromedriver.exe'
COOKIES='_hc.v=480b2d65-9e8e-472b-6c4a-54594e6d6c17.1653489029; _lxsdk=180fba04f86c8-0aa06f0883805b-14333270-1fa400-180fba04f87c8; _lxsdk_cuid=180fba04f86c8-0aa06f0883805b-14333270-1fa400-180fba04f87c8; ctu=a3043854820c5ca48a27b05d5b3b41e9699b4ca177aafd1f93ba24fa0c9b230b; default_ab=ugcdetail:A:1; fspop=test; s_ViewType=10; cye=shanghai; cy=1; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1654510162,1654575628,1654656139,1654695386; WEBDFPID=y04z99z17z0w53w11xw8w27xv5029z8z818561z47uz97958616875zx-1654781947997-1654695546077EUGEGOOfd79fef3d01d5e9aadc18ccd4d0c95072758; _lx_utm=utm_source=Baidu&utm_medium=organic; dplet=eefb471e43d3e9ed1b8787643eb20137; dper=23465715ed12bb9358208a9915300ef44b2e58821bd8ee3a35ff61cce743618569611e01de3d5cdc87dc89d76653d0e07656421564b2a5c950df8d5db07f0f8c5325067dea630c159f0f197ad222d4dc19f80dcf0e2d221f93725b7a9d803dcf; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_1526924156; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1654703296; _lxsdk_s=18143e19a02-601-714-535||979'
f = open('ceshi.txt','wb+')
class DianpingComment:
    font_size = 14
    start_y = 23
    def __init__(self, shop_id, cookies, delay=7, handle_ban=True,comments =comments):
        self.shop_id = shop_id
        self._delay = delay
        self.num = 1
        self.db =comments
        self._cookies = self._format_cookies(cookies)
        self._css_headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
        self._default_headers = {
            'Connection': 'keep-alive',
            'Host': 'www.dianping.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            'Cookie':'_hc.v=480b2d65-9e8e-472b-6c4a-54594e6d6c17.1653489029; _lxsdk=180fba04f86c8-0aa06f0883805b-14333270-1fa400-180fba04f87c8; _lxsdk_cuid=180fba04f86c8-0aa06f0883805b-14333270-1fa400-180fba04f87c8; ctu=a3043854820c5ca48a27b05d5b3b41e9699b4ca177aafd1f93ba24fa0c9b230b; default_ab=ugcdetail:A:1; fspop=test; s_ViewType=10; cye=shanghai; cy=1; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1654510162,1654575628,1654656139,1654695386; WEBDFPID=y04z99z17z0w53w11xw8w27xv5029z8z818561z47uz97958616875zx-1654781947997-1654695546077EUGEGOOfd79fef3d01d5e9aadc18ccd4d0c95072758; _lx_utm=utm_source=Baidu&utm_medium=organic; dplet=eefb471e43d3e9ed1b8787643eb20137; dper=23465715ed12bb9358208a9915300ef44b2e58821bd8ee3a35ff61cce743618569611e01de3d5cdc87dc89d76653d0e07656421564b2a5c950df8d5db07f0f8c5325067dea630c159f0f197ad222d4dc19f80dcf0e2d221f93725b7a9d803dcf; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_1526924156; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1654703296; _lxsdk_s=18143e19a02-601-714-535||979'}
        self._cur_request_url ='http://www.dianping.com/shop/{}/review_all'.format(self.shop_id)
        self.sub_url ='http://www.dianping.com'
    def run(self):
        self._css_link = self._get_css_link(self._cur_request_url)
        self._font_dict = self._get_font_dict(self._css_link)
        self._get_conment_page()
    def _delay_func(self):
        delay_time = random.randint((self._delay - 2) * 10, (self._delay + 2) * 10) * 0.1
        time.sleep(delay_time)
    def _init_browser(self):
        """
            初始化游览器
        """
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        browser = webdriver.Chrome(chrome_options=chrome_options,executable_path=path_one)
        browser.get(self._cur_request_url)
        for name, value in self._cookies.items():
            browser.add_cookie({'name': name, 'value': value})
        browser.refresh()
        return browser
    def _handle_ban(self):
        """
            爬取速度过快，出现异常时处理验证
        """
        try:
            self._browser.refresh()
            time.sleep(1)
            button = self._browser.find_element_by_id('yodaBox')
            move_x_offset = self._browser.find_element_by_id('yodaBoxWrapper').size['width']
            webdriver.ActionChains(self._browser).drag_and_drop_by_offset(
                button, move_x_offset, 0).perform()
        except:
            pass
    def _format_cookies(self, cookies):
        '''
        获取cookies;;;
        :param cookies:
        :return:
        '''
        cookies = {cookie.split('=')[0]: cookie.split('=')[1]
                   for cookie in cookies.replace(' ', '').split(';')}
        return cookies

    def _get_conment_page(self):
        """
            请求评论页，并将<span></span>样式替换成文字;
        """
        while self._cur_request_url:
            self._delay_func()
            print('_cur_request_url:{}'.format(self._cur_request_url))
            print('[{now_time}] {msg}'.format(now_time=datetime.datetime.now(), msg=self._cur_request_url))
            res = requests.get(self._cur_request_url, headers=self._default_headers, cookies=self._cookies)

            while res.status_code !=200:
                cookie = random.choice(COOKIES)
                cookies = self._format_cookies(cookie)
                res = requests.get(self._cur_request_url, headers=self._default_headers, cookies=cookies)
                if res.status_code == 200:
                    break
            html = res.text

            class_set = []
            for span in re.findall(r'<svgmtsi class="([a-zA-Z0-9]{5,6})"></svgmtsi>', html):
                class_set.append(span)
            for class_name in class_set:
                try:
                    print("class_name："+str(class_name)+"_font_dict:"+str(self._font_dict[class_name]))

                    html = re.sub('<svgmtsi class="%s"></svgmtsi>' % class_name, self._font_dict[class_name], html)
                    print('{}已替换完毕_______________________________'.format(self._font_dict[class_name]))
                except:
                    html = re.sub('<svgmtsi class="%s"></svgmtsi>' % class_name, '', html)
                    print('替换失败…………………………………………………………………………&&&&&&&&&&&&&&&&&&&&&&&&')
            doc = pq(html)
            self._parse_comment_page(html)
            if  doc('.NextPage').attr('href'):
                self._default_headers['Referer'] = self._cur_request_url
                next_page_url1 = doc('.NextPage').attr('href')
                next_page_url =self.sub_url +  str(next_page_url1)
                print('next_url:{}'.format(next_page_url))
            else:
                next_page_url = None
                # with open('est2.txt', 'a+',newline='',encoding='utf-8') as f:
                #     writer=f.write(res.text)



                # with open("test2.txt",a+)
                # print(res.text)
                # self._handle_ban()
                # self._get_conment_page()
            print('next_page_url:{}'.format(next_page_url))
            self._cur_request_url = next_page_url



    def _data_pipeline(self, data):
        """
            处理数据
        """
        print(data)

    def _parse_comment_page(self, html):
        """
            解析评论页并提取数据,把数据写入文件中；；
        """
        doc =pq(html)
        for li in doc('div.review-list-main > div.reviews-wrapper > div.reviews-items > ul > li'):

            doc_text =pq(li)
            if doc_text('.dper-info .name').text():
                name = doc_text('.dper-info .name').text()
            else:
                name = None
            try:
                star = doc_text('.review-rank .sml-rank-stars').attr('class')

            except IndexError:
                star = None
            if doc_text('div.misc-info.clearfix > .time').text():
                date_time =doc_text('div.misc-info.clearfix > .time').text()
            else:
                date_time=None
            if doc_text('.main-review .review-words').text():
                comment =doc_text('.main-review .review-words').text()
            else:
                comment=None

            data = {
                'name': name,
                'date_time':date_time,
                'star': star,
                'comment':comment
            }
            print(data)
            f.write(str(data).encode('utf-8'))
            print('写入数据完成',data)


    def _get_css_link(self, url):
        """
            请求评论首页，获取css样式文件
        """
        try:
            # print(url)
            res = requests.get(url, headers=self._default_headers, cookies = self._cookies)
            html = res.text
            css_link = re.search(r'<link re.*?css.*?href="(.*?svgtextcss.*?)">', html)
            # print(css_link)
            assert css_link
            css_link = 'http:' + css_link[1]
            return css_link
        except:
            None

    def _get_font_dict(self, url):
        """
            获取css样式对应文字的字典
        """
        res = requests.get(url, headers=self._css_headers)
        html = res.text

        background_image_link = re.findall(r'background-image:.*?\((.*?svg)\)', html)
        # print(background_image_link)
        background_image_link_list =[]
        for i in background_image_link:
            url ='http:'+i
            background_image_link_list.append(url)

        # print(background_image_link_list)

        html = re.sub(r'span.*?\}', '', html)
        group_offset_list = re.findall(r'\.([a-zA-Z0-9]{5,6}).*?round:(.*?)px (.*?)px;', html)
        '''
        多个偏移字典，合并在一起；；；
        '''
        font_dict_by_offset_list ={}
        for i in background_image_link_list:

            font_dict_by_offset_list.update(self._get_font_dict_by_offset(i))

        font_dict_by_offset = font_dict_by_offset_list


        font_dict = {}
        for class_name, x_offset, y_offset in group_offset_list:
            x_offset = x_offset.replace('.0', '')
            y_offset = y_offset.replace('.0', '')
            try:
                font_dict[class_name] = font_dict_by_offset[int(y_offset)][int(x_offset)]

            except:
                font_dict[class_name] = ''
        return font_dict

    def _get_font_dict_by_offset(self, url):
        """
            获取坐标偏移的文字字典, 会有最少两种形式的svg文件（目前只遇到两种）
        """
        res = requests.get(url, headers=self._css_headers)
        html = res.text
        font_dict = {}
        y_list = re.findall(r'd="M0 (\d+?) ', html)
        if y_list:
            font_list = re.findall(r'<textPath .*?>(.*?)<', html)
            for i, string in enumerate(font_list):
                y_offset = self.start_y - int(y_list[i])

                sub_font_dict = {}
                for j, font in enumerate(string):
                    x_offset = -j * self.font_size
                    sub_font_dict[x_offset] = font
                font_dict[y_offset] = sub_font_dict
        else:
            font_list = re.findall(r'<text.*?y="(.*?)">(.*?)<', html)
            for y, string in font_list:
                y_offset = self.start_y - int(y)
                sub_font_dict = {}
                for j, font in enumerate(string):
                    x_offset = -j * self.font_size
                    sub_font_dict[x_offset] = font
                font_dict[y_offset] = sub_font_dict
        return font_dict
    def test(self):
        # dianping = Customer('4114867', cookies=COOKIES)
        # dianping.run()
        # f.close()
        url="http://www.dianping.com/shop/G85MfSgR7HCkqHMx/review_all/p2"
        res = requests.get(url, headers=self._default_headers, cookies=self._cookies)
        print(res.text)
class Customer(DianpingComment):
    def _data_pipeline(self, data):
        print(data)
#
if __name__ == "__main__":
    dianping = Customer('4114867', cookies=COOKIES)
    dianping.run()
    f.close()