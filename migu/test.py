import json
import execjs
import requests

class Migu_login(object):

    def __init__(self, account, password):
        modulus = '00833c4af965ff7a8409f8b5d5a83d87f2f19d7c1eb40dc59a98d2346cbb145046b2c6facc25b5cc363443f0f7ebd9524b7c1e1917bf7d849212339f6c1d3711b115ecb20f0c89fc2182a985ea28cbb4adf6a321ff7e715ba9b8d7261d1c140485df3b705247a70c28c9068caabbedbf9510dada6d13d99e57642b853a73406817'
        publicExponent = '010001'
        # details_params 生成加密指纹的参数
        details_params = '''{"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/84.0.4147.13","language":"zh-CN","color_depth":"24","pixel_ratio":"1","hardware_concurrency":"8","resolution":"1600,900","available_resolution":"1600,860","timezone_offset":"-480","session_storage":"1","local_storage":"1","indexed_db":"1","open_database":"1","cpu_class":"unknown","navigator_platform":"Win32","do_not_track":"unknown","regular_plugins":"ChromePDFPlugin::Portable Document Format::application/x-google-chrome-pdf~pdf,ChromePDFViewer::","webgl_vendor":"GoogleInc.~ANGLE(NVIDIAGeForceGTX1660SUPERDirect3D11vs_5_0ps_5_0)","adblock":"false","has_lied_languages":"false","has_lied_resolution":"false","has_lied_os":"false","has_lied_browser":"false","touch_support":"0,false,false","js_fonts":"Arial,Arial Black,Arial Narrow,Calibri,Cambria,Cambria Math,Comic Sans MS,Consolas,Courier,Courier N"}'''
        # result_params 生成加密指纹的参数
        result_params = 'c4d33230e09fadc2be27358ea4c9d9b5'
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Referer': 'https://passport.migu.cn/login?sourceid=100001&apptype=0&forceAuthn=false&isPassive=false&authType=MiguPassport&' \
                       'passwordControl=0&display=web&referer=https://passport.migu.cn/&logintype=1&qq=null&weibo=null&alipay=null&' \
                       'weixin=null&andPass=null&phoneNumber=&callbackURL=&relayState=',
            'Host': 'passport.migu.cn',
            'Origin': 'https://passport.migu.cn',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        self.form = {
            'sourceID': '208003',
            'appType': '0',
            'relayState': '',
            'loginID': '',                      # 加密的账号
            'enpassword': '',                   # 加密的密码
            'captcha': '',
            'imgcodeType': '',
            'fingerPrint': '',                  # 指纹
            'fingerPrintDetail': '',            # 指纹detail
            'isAsync': True
        }
        self.session = requests.Session()
        self.session.headers = headers
        self.get_cookies()

        self.js_object = self.compile_js()
        # 这里需要把js代码中返回值的key改成表单中相应的指纹字段
        update_form = self.make_rsa_fingerprint(modulus, publicExponent, details_params, result_params)
        update_form['enpassword'] = self.make_encrypt_password(password, modulus, publicExponent)
        update_form['loginID'] = self.make_encrypt_account(account, modulus, publicExponent)
        self.form.update(update_form)

    def get_cookies(self):
        url_list = ['https://passport.migu.cn/', 'https://passport.migu.cn/user/nav']
        for url in url_list:
            self.session.get(url)

        return self.session.cookies

    def compile_js(self):
        with open('rsa.js', 'r',encoding="utf_8") as f:
            js = f.read()

        return execjs.compile(js)

    def make_rsa_fingerprint(self, modulus, publicExponent, details, result):
        """生成rsa指纹参数

        Args:
            details (str): 请求headers信息
            result (str): headers的加密信息，如果headers不改变这个值也是固定的

        Returns (dict):
            details: 加密后的fingerprint_details信息，fingerPrintDetail表单参数
            result: 加密后的fingerprint_result信息，fingerPrint表单参数
        """
        return self.js_object.call('rsaFingerprint', modulus, publicExponent, details, result)

    def make_encrypt_password(self, password, modulus, publicExponent):
        """生成加密后的密码

        Args:
            password (str): 输入框内输入的原始密码
            modulus (str): rsa加密参数，两个质数的乘积，固定值，前一个请求获得
            publicExponent (str): rsa加密参数，大于1的奇数，固定值，前一个请求获得

        Returns:
            str: 加密后的密码
        """
        return self.js_object.call('getEncryptedPwd', password, modulus, publicExponent)

    def make_encrypt_account(self, account, modulus, publicExponent):
        """生成加密后的密码

        Args:
            account (str): 输入框内输入的密码
            modulus (str): 同上
            publicExponent (str): 同上

        Returns:
            str: 加密后的账号
        """
        return self.js_object.call('getEncryptedAccount', account, modulus, publicExponent)

    def login(self):
        url = 'https://passport.migu.cn/authn'
        response = self.session.post(url, data=self.form)    # print(self.form)
        # print(response.text)

        # 返回的字典内容
        # {
        #   "status":2000,
        #   "message":"",
        #   "header":{"resultcode":"104000"},
        #   "result":{
        #       "risk_resultCode":"00000",
        #       "redirectURL":"https://passport.migu.cn/portal/sso/authn",
        #       "authNType":"MiguPassport",
        #       "risk_LevelCode":"0",
        #       "risk_ruleCode":"00000000",
        #       "risk_measureCode":"000000",
        #       "token":"STnid00000115987905238740vZwyvSelvgKxuYj7KISYT6xzfqPhTuW"
        #   }
        # }
        response_dict = json.loads(response.text)
        redirect_url = response_dict.get('result', {}).get('redirectURL', '')
        token = response_dict.get('result', {}).get('token', '')

        if not redirect_url or not token:
            return

        rest_url = [
            redirect_url + '?callbackURL=&relayState=&token={}'.format(token),
            'https://passport.migu.cn/portal/sso/authn_success?relateToMiguPassport=1&callbackURL=&relayState=',
            'https://passport.migu.cn/portal/home/profile?sourceid=100001',
            ]
        for ru in rest_url:
            response = self.session.get(ru)
        response=self.session.get("https://passport.migu.cn/portal/home/profile?sourceid=100001")

        return response


if __name__ == '__main__':
    maccount = input('账号:')
    mpassword = input('密码:')
    mg = Migu_login(maccount, mpassword)
    mresponse = mg.login()
    print(mresponse.text)

