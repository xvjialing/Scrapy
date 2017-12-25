import requests
import time

try:
    import cookielib
except:
    import http.cookiejar as cookielib

import re

agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) Gecko/20100101 Firefox/57.0"

header={
    "Host":"www.zhihu.com",
    "Referer":"https://www.zhihu.com/",
    "User-Agent":agent
}

session=requests.session()

def get_xsrf():
    #获取xsrf
    response = session.get("https://www.zhihu.com/#signin",headers=header)

    txt=response.text
    # txt='<input type="hidden" name="_xsrf" value="44f233261dce4bcb078968b66c3e25f0"/>'
    # print(txt)
    xsrf = re.match('.*name="_xsrf" value="(.*?)"',txt,re.S)
    if xsrf:
        xsrf= xsrf.group(1)
    print(xsrf)

    return xsrf



def zhihu_login(account,password):
    # 知乎登陆
    if re.match("^1\d{10}",account):
        print("手机号登陆")
        post_url= "https://www.zhihu.com/login/phone_num"
        post_data = {
            "_xsrf": get_xsrf(),
            "password": password,
            "captcha_type": "cn",
            "phone_num": account
        }
        response=session.post(post_url,post_data,headers=header)
        session.cookies.save()
        print(response.text)



zhihu_login("18768379083","xjl1994920")
# get_xsrf()

