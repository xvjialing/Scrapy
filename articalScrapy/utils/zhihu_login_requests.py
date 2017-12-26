import json

import requests
import time

try:
    import cookielib
except:
    import http.cookiejar as cookielib

import re
from PIL import Image

agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) Gecko/20100101 Firefox/57.0"

# 该captcha_url用于打开知乎验证码图片
captcha_url = 'https://www.zhihu.com/captcha.gif?r=%d&type=login' % (time.time() * 1000)

header={
    "Host":"www.zhihu.com",
    "Referer":"https://www.zhihu.com/",
    "User-Agent":agent,
}

session=requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies.txt')
try:
    session.cookies.load(ignore_discard=True)
except:
    print("cookie未能加载")

def get_index():
    response = session.get("https://www.zhihu.com/#signin", headers=header)
    with open("index_page.html","wb") as f:
        f.write(response.text.encode("utf-8"))
    print("ok")

def get_xsrf():
    #获取xsrf
    response = session.get("https://www.zhihu.com/#signin",headers=header)

    txt=response.text

    xsrf = re.match('.*name="_xsrf" value="(.*?)"',txt,re.S)
    if xsrf:
        xsrf= xsrf.group(1)

    return xsrf

def is_login():
    # 通过个人中心页面的状态码判断是否登陆
    inbox_url="https://www.zhihu.com/inbox"
    response= session.get(inbox_url,headers=header,allow_redirects=False)
    if response.status_code != 200:
        return False
    else:
        return True


def get_captcha():
    # 获取验证码
    t = str(int(time.time() * 1000))
    captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
    response = session.get(captcha_url, headers=header)
    captcha_name = 'captcha.gif'
    with open(captcha_name, 'wb') as f:
        f.write(response.content)
    im = Image.open(captcha_name)
    im.show()
    return input('请输入验证码: ')


def zhihu_login(account,password):
    # 知乎登陆
    if re.match("^1\d{10}",account):
        print("手机号登陆")
        post_url= "https://www.zhihu.com/login/phone_num"
        post_data = {
            "_xsrf": get_xsrf(),
            "password": password,
            "captcha": get_captcha(),
            "phone_num": account,
        }
    else:
        if "@" in account:
            print("邮箱登陆")
            post_url = "https://www.zhihu.com/login/email"
            post_data = {
                "_xsrf": get_xsrf(),
                "password": password,
                "captcha": get_captcha(),
                "email": account,
            }
    response = session.post(post_url, post_data, headers=header)
    print(response.text)
    session.cookies.save()
    # jsontext = json.loads(response.text)
    # print(jsontext)

# zhihu_login("11111111","11111111")

# get_index()
is_login()
