
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
path_one = r'C:\Users\FREEDOM\AppData\Local\Google\Chrome\Application\chromedriver.exe'
COOKIES='_hc.v=480b2d65-9e8e-472b-6c4a-54594e6d6c17.1653489029; _lxsdk=180fba04f86c8-0aa06f0883805b-14333270-1fa400-180fba04f87c8; _lxsdk_cuid=180fba04f86c8-0aa06f0883805b-14333270-1fa400-180fba04f87c8; ctu=a3043854820c5ca48a27b05d5b3b41e9699b4ca177aafd1f93ba24fa0c9b230b; default_ab=ugcdetail:A:1; fspop=test; s_ViewType=10; cye=shanghai; cy=1; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1654272926,1654488233,1654510162,1654575628; WEBDFPID=z65w285895865u6xz5uwv2wxz9y299w18186x3211849795878u091yy-1654662227043-1654575825812WSUKCMSfd79fef3d01d5e9aadc18ccd4d0c95077203; dplet=eb0f9b4276ac275d71af48fca163810f; dper=23465715ed12bb9358208a9915300ef4745202f438967f06a939b9999f361df6c24d91e1eda89b64f5c74b28780750c7bb49d62f0fc24ca819aacbd9e87f7f92468c231e6c93d268a3c49afeb8e251eef4796f5272e701a0cad0a92a806cd0ee; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_1526924156; _lx_utm=utm_source=Baidu&utm_medium=organic; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1654600071; _lxsdk_s=1813dd972f6-df7-26d-b17||4'
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
            'Cookie':'_lxsdk_cuid=16beb593744c8-082d3569f1b8da-e343166-100200-16beb593745c8; _lxsdk=16beb593744c8-082d3569f1b8da-e343166-100200-16beb593745c8; _hc.v=ead7aff3-40db-cb98-55ad-5460a0d10d6b.1563021622; s_ViewType=10; ua=zeroing; ctu=66a794ac79d236ecce433a9dd7bbb8bfac5ea81a9b7f2bdd8fe4eebbf54d3360; cy=169; cye=xuchang; dper=56cacd1d2e3f2645cfb85b48c96050d14127f349ac745cbe31b284282d72cf8960cfac5e2905d189386b038519f242d87f018031896f95f41ea215722b177d0d6619908c98d99eac35b14c560bc15035e0dc1d79e6dafff624d52dbb63d82db9; ll=7fd06e815b796be3df069dec7836c3df; uamo=13243174991; _lxsdk_s=16cbdc7eed1-542-97e-b28%7C%7C664' }
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
            # print(css_link)
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

        # html = re.sub(r'span.*?\}', '', html)
        # print(html)
        group_offset_list = re.findall(r'\.([a-zA-Z0-9]{5,6}).*?round:(.*?)px (.*?)px;', html)
        # print("group_offset_list")
        # print(group_offset_list)
        '''
        多个偏移字典，合并在一起；；；
        '''
        font_dict_by_offset_list ={}
        for i in background_image_link_list:

            font_dict_by_offset_list.update(self._get_font_dict_by_offset(i))

        font_dict_by_offset = font_dict_by_offset_list
        # print(font_dict_by_offset)
        font_dict = {}
        for class_name, x_offset, y_offset in group_offset_list:
            x_offset = x_offset.replace('.0', '')
            y_offset = y_offset.replace('.0', '')
            try:
                font_dict[class_name] = font_dict_by_offset[int(y_offset)][int(x_offset)]

            except:
                font_dict[class_name] = ''
        print(font_dict)
        return font_dict

    def _get_font_dict_by_offset(self, url):
        """
            获取坐标偏移的文字字典, 会有最少两种形式的svg文件（目前只遇到两种）
        """
        res = requests.get(url, headers=self._css_headers)
        html = res.text
        font_dict = {}
        y_list = re.findall(r'd="M0 (\d+?) ', html)
        # print(y_list)
        if y_list:
            font_list = re.findall(r'<textPath .*?>(.*?)<', html)
            for i, string in enumerate(font_list):
                y_offset = self.start_y - int(y_list[i])
                # print("y:"+str(y_offset))
                sub_font_dict = {}
                for j, font in enumerate(string):
                    x_offset = -j * self.font_size
                    sub_font_dict[x_offset] = font
                font_dict[y_offset] = sub_font_dict
            print("*"*20)
            print("font_dict1")
            print(font_dict)
        else:
            font_list = re.findall(r'<text.*?y="(.*?)">(.*?)<', html)
            for y, string in font_list:
                y_offset = self.start_y - int(y)
                sub_font_dict = {}
                for j, font in enumerate(string):
                    x_offset = -j * self.font_size
                    sub_font_dict[x_offset] = font
                font_dict[y_offset] = sub_font_dict
            print("*"*20)
            print("font_dict")
            print(font_dict)
        return font_dict

class Customer(DianpingComment):
    def _data_pipeline(self, data):
        print(data)
if __name__ == "__main__":

   dp=DianpingComment('4114867', cookies=COOKIES)
   s=dp._get_css_link(dp._cur_request_url)
   dp._get_font_dict(s)
   # dp._get_font_dict_by_offset('http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/7272eaf5d685f2131faad571e1de2fc5.svg')