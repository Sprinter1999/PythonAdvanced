import re
import os
import json
import requests

s = requests.Session()
# cookies序列化文件
COOKIES_FILE_PATH = 'taobao_login_cookies.txt'

class TaoBaoLogin:

    def __init__(self, session):
        """
        账号登录对象
        :param username: 用户名
        :param ua: 淘宝的ua参数
        :param TPL_password2: 加密后的密码
        """
        # 检测是否需要验证码的URL
        self.user_check_url = 'https://login.taobao.com/member/request_nick_check.do?_input_charset=utf-8'
        # 验证淘宝用户名密码URL
        self.verify_password_url = "https://login.taobao.com/member/login.jhtml"
        # 访问st码URL
        self.vst_url = 'https://login.taobao.com/member/vst.htm?st={}'
        # 淘宝个人 主页
        self.my_taobao_url = 'http://i.taobao.com/my_taobao.htm'

        # 淘宝用户名
        self.username = '18859569188'
        # 淘宝重要参数，从浏览器或抓包工具中复制，可重复使用
        self.ua = '122#VxpZZ4aBEE+x1EpZMEpJEJponDJE7SNEEP7rEJ+/f9t/2oQLpo7iEDpWnDEeK51HpyGZp9hBuDEEJFOPpC76EJponDJL7gNpEPXZpJRgu4Ep+FQLpoGUEJLWn4yP7SQEEyuLpERDI8v6prZCnaRx9kb/hel0jhFuI1AY31qjwFsYAuR8qwtwOVAn/AQ1l4EzFqcLIUaJGYB8Tt6Wv/EU/3r18k55n6nXPwQvunBSIsx/nMj72844DahvyQglXE3OM2kd/GZUDDPieSp1uOo8RRWlzBC01DIEyF3K40LpGlLMBnRhuOqEELVZ8opwJzVF64OUqW32DEVJnSL1ethHqchH8CL638EEyFftqSfbDEpxnSp1uOIEELXZGoLUJDbEyF3mqW32E5pxngL4ul0EDLVr88A6JNbWCofDqW3Zp8C0nURu+tOUzRm1v4enNzGsGRkP+8k/DLv+X9LGEPNsJkHrfuILTPFxj7msiC1ulh25e2sd6bmHPMfp8k3AfpktHAlFCLAmAEHGEDF38Md4KPtvi/RvwRsRUo+QH50pFl7rgcY1dLS6zNi9gXiXStMRZ3PjJJRRZTK8YYe47LsX0DRI0RuYd9vKsJg3PL2uQXGkHzaBdYu3WyDaniQ3Q976ro5bV9nmi91zzehP4VVQG8ZXjXGNU9g6z8cCf8qWKB+5tXk934GTRvCF0yLBaCvGIf4pfK1qPjeu0LWN615p1FOdeFIv6Sf0kCz4vDW2BLwo8qFReecBfgke5PEWxtVAY82vIoBa8i+tuXm7iBFrEZh125Fpqg1B1g6BYO+u7s5HrLq76D7hCfRjG25QNTcTJzEH56eY1EnLDnFejqdrP3FDMC0K1sg52xyavzY8zo8R6hkjgaEfkVKtPKOvJtvCFCUO3S4ebUH6cjQSJwOSEQVe4fyj66QH054Cqt6j1Apk9bDObgUIZwdl3ks/KTpjAVjA8wyQ3EjO3OUZ1ONnI5qtVs4xHV2qS3rAqjZpgbG3flB0p6QiQYBODIcqWpDN6NabLSxNLu820Bnfsj/N4k/7oZ4MWliIWjG0jgcy6+MgUgULCk3BI/T23ydgPs0Zm55RfVFUBw/Qbu6JP1uen1C+qbG5X6g9OOYIDyZDKUT2j6OI9l0ps74Corm75/vyGPhIP2pfY84fzvFi96wabm5HiMABatc3DPGHuuXmYkUeSI1PDX6i0rR0/wrcOHonyDk6H5t4Dlgo/iQ6fmIOrfkAGk7seXxmBtHGKDz/yV01UvjIvtAze+jK/7XhR48mkYPF+Tii3/SymfYfc3MLdQ3lwvySvtXAW+Ar8mvsyDu2sq4n/ZOkc4CVr6O/1ALsssv5J3dlfBVE4EW4ZbzYEVXPsmi5vQj0I3FAT2GpCcaX6yomEtQiAKoSks+KamheODHXB2fIc1jQCST6wdDO8Myg0Uuu3Iqbhpxh4MoyngCSRsUfwPbTFNOfNdL+Ay1pXYJoYMBx2SNj3mfdO251XYEuep0YMnptbloHY5Jf95pJy2ic7LwwCwEYpiiJJlFTGv2CdCj/Tr2AGNZwpx2arxfguFXILzKUdQsNfAw+oYB5/b/1KW3KeOxv+MdtwqK9o97j2vs8cg6Fr4Kz2FBtL8/nP4=='
        # 加密后的密码，从浏览器或抓包工具中复制，可重复使用
        self.TPL_password2 = '33dbf34383c8fd8d7c0a36d8eb6dbf151b9dd7534972d96fab42396923d5c58d7bc2a2e2235f050df00bac0a24ed916a9c451f1001570ac4b90dd4f1c6f557b46e344156c06e21b579ae73da5f6b94c074fd9f8a533b4c3e9b3589373c26e7503af263ddbc024d7853cde9b245207db90cfd63dd0385e1d5b22c1f284a5c1e23'
        # 请求超时时间
        self.timeout = 3
        # session对象，用于共享cookies
        self.session = session

        if not self.username:
            raise RuntimeError('请填写你的淘宝用户名')

    def _user_check(self):
        """
        检测账号是否需要验证码
        :return:
        """
        data = {
            'username': self.username,
            'ua': self.ua
        }
        try:
            response = self.session.post(self.user_check_url, data=data, timeout=self.timeout)
            response.raise_for_status()
        except Exception as e:
            print('检测是否需要验证码请求失败，原因：')
            raise e
        needcode = response.json()['needcode']
        print('是否需要滑块验证：{}'.format(needcode))
        return needcode


    def _verify_password(self):
        verify_password_headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Origin': 'https://login.taobao.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://login.taobao.com/member/login.jhtml?spm=a230r.1.754894437.1.33236fbeDeeQnj&f=top&redirectURL=https%3A%2F%2Fs.taobao.com%2Fsearch%3Fq%3D%25E6%2589%258B%25E6%259C%25BA%26imgfile%3D%26commend%3Dall%26ssid%3Ds5-e%26search_type%3Ditem%26sourceId%3Dtb.index%26spm%3Da21bo.2017.201856-taobao-item.1%26ie%3Dutf8%26initiative_id%3Dtbindexz_20170306%26sort%3Dsale-desc',
        }
        # 登录toabao.com提交的数据，如果登录失败，可以从浏览器复制你的form data
        verify_password_data = {
            'TPL_username': self.username,
            'ncoToken': '52a4fbd4714a40af97373f92af9361b509d2858b',
            'slideCodeShow': 'false',
            'useMobile': 'false',
            'lang': 'zh_CN',
            'loginsite': 0,
            'newlogin': 0,
            'TPL_redirect_url': 'https://www.taobao.com/',
            'from': 'tb',
            'fc': 'default',
            'style': 'default',
            'keyLogin': 'false',
            'qrLogin': 'true',
            'newMini': 'false',
            'newMini2': 'false',
            'loginType': '3',
            'gvfdcname': '10',
            'gvfdcre': '68747470733A2F2F732E74616F62616F2E636F6D2F7365617263683F713D25453625383925384225453625394325424126696D6766696C653D26636F6D6D656E643D616C6C26737369643D73352D65267365617263685F747970653D6974656D26736F7572636549643D74622E696E6465782673706D3D613231626F2E323031372E3230313835362D74616F62616F2D6974656D2E312669653D7574663826696E69746961746976655F69643D7462696E6465787A5F323031373033303626736F72743D73616C652D64657363',
            'TPL_password_2': self.TPL_password2,
            'loginASR': '1',
            'loginASRSuc': '1',
            'oslanguage': 'zh-CN',
            'sr': '1920*1080',
            'osVer': '',
            'naviVer': 'chrome|77.0394588',
            'osACN': 'Mozilla',
            'osAV': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            'osPF': 'Win32',
            'appkey': '00000000',
            'mobileLoginLink': 'https://login.taobao.com/member/login.jhtml?spm=a230r.1.754894437.1.33236fbeDeeQnj&f=top&redirectURL=https://s.taobao.com/search?q=%E6%89%8B%E6%9C%BA&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&sort=sale-desc&useMobile=true',
            'showAssistantLink': '',
            'um_token': 'TBC4FF5517842F8F053FFDF0633BC16654899C09F9796404352DD657383',
            'ua': self.ua
        }
        try:
            response = self.session.post(self.verify_password_url, headers=verify_password_headers, data=verify_password_data,
                              timeout=self.timeout)
            response.raise_for_status()
            # 从返回的页面中提取申请st码地址
        except Exception as e:
            print('验证用户名和密码请求失败，原因：')
            raise e
        # 提取申请st码url
        apply_st_url_match = re.search(r'<script src="(.*?)"></script>', response.text)
        # 存在则返回
        if apply_st_url_match:
            print('验证用户名密码成功，st码申请地址：{}'.format(apply_st_url_match.group(1)))
            return apply_st_url_match.group(1)
        else:
            raise RuntimeError('用户名密码验证失败！response：{}'.format(response.text))

    def _apply_st(self):
        """
        申请st码
        :return: st码
        """
        apply_st_url = self._verify_password()
        try:
            response = self.session.get(apply_st_url)
            response.raise_for_status()
        except Exception as e:
            print('申请st码请求失败，原因：')
            raise e
        st_match = re.search(r'"data":{"st":"(.*?)"}', response.text)
        if st_match:
            print('获取st码成功，st码：{}'.format(st_match.group(1)))
            return st_match.group(1)
        else:
            raise RuntimeError('获取st码失败！response：{}'.format(response.text))

    def login(self):
        """
        使用st码登录
        :return:
        """
        # 加载cookies文件
        if self._load_cookies():
            return True
        # 判断是否需要滑块验证
        self._user_check()
        st = self._apply_st()
        headers = {
            'Host': 'login.taobao.com',
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
        }
        try:
            response = self.session.get(self.vst_url.format(st), headers=headers)
            response.raise_for_status()
        except Exception as e:
            print('st码登录请求，原因：')
            raise e
        # 登录成功，提取跳转淘宝用户主页url
        my_taobao_match = re.search(r'top.location.href = "(.*?)"', response.text)
        if my_taobao_match:
            print('登录淘宝成功，跳转链接：{}'.format(my_taobao_match.group(1)))
            self._serialization_cookies()
            return True
        else:
            raise RuntimeError('登录失败！response：{}'.format(response.text))

    def _load_cookies(self):
        # 1、判断cookies序列化文件是否存在
        if not os.path.exists(COOKIES_FILE_PATH):
            return False
        # 2、加载cookies
        self.session.cookies = self._deserialization_cookies()
        # 3、判断cookies是否过期
        try:
            self.get_taobao_nick_name()
        except Exception as e:
            os.remove(COOKIES_FILE_PATH)
            print('cookies过期，删除cookies文件！')
            return False
        print('加载淘宝登录cookies成功!!!')
        return True

    def _serialization_cookies(self):
        """
        序列化cookies
        :return:
        """
        cookies_dict = requests.utils.dict_from_cookiejar(self.session.cookies)
        with open(COOKIES_FILE_PATH, 'w+', encoding='utf-8') as file:
            json.dump(cookies_dict, file)
            print('保存cookies文件成功！')

    def _deserialization_cookies(self):
        """
        反序列化cookies
        :return:
        """
        with open(COOKIES_FILE_PATH, 'r+', encoding='utf-8') as file:
            cookies_dict = json.load(file)
            cookies = requests.utils.cookiejar_from_dict(cookies_dict)
            return cookies

    def get_taobao_nick_name(self):
        """
        获取淘宝昵称
        :return: 淘宝昵称
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
        }
        try:
            response = self.session.get(self.my_taobao_url, headers=headers)
            response.raise_for_status()
        except Exception as e:
            print('获取淘宝主页请求失败！原因：')
            raise e
        # 提取淘宝昵称
        nick_name_match = re.search(r'<input id="mtb-nickname" type="hidden" value="(.*?)"/>', response.text)
        if nick_name_match:
            print('登录淘宝成功，你的用户名是：{}'.format(nick_name_match.group(1)))
            return nick_name_match.group(1)
        else:
            raise RuntimeError('获取淘宝昵称失败！response：{}'.format(response.text))


if __name__ == '__main__':
    ul = TaoBaoLogin(s)
    ul.login()
    ul.get_taobao_nick_name()