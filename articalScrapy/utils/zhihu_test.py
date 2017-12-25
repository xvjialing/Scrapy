#coding:utf-8
import re
# from bs4 import BeautifulSoup
import gzip
import urllib.request
import urllib.parse
import http.cookiejar
import ssl
import time
import requests

heads={
            "Accept":"text/html, application/xhtml+xml, */*",
            "Accept-Language":"zh-CN",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0",
            "Accept-Encoding": "gzip, deflate",
            "Host": "www.zhihu.com",
            "DNT": "1",
            "Connection": "Keep-Alive"
            }

def get_opener(heads):
    cj=http.cookiejar.CookieJar()
    pro=urllib.request.HTTPCookieProcessor(cj)
    opener=urllib.request.build_opener(pro)
    header=[]
    for key,value in heads.items():
        header.append((key,value))
    opener.addheaders=header
    return opener

def ungzip(data):
    try:
        print("正在解压....")
        data=gzip.decompress(data)
        print("解压完成")
    except:
        print("无需解压")
    return data

def get_xsrf():
    #获取xsrf
    response = requests.get("https://www.zhihu.com/#signin",headers=heads)

    txt=response.text
    # txt='<input type="hidden" name="_xsrf" value="44f233261dce4bcb078968b66c3e25f0"/>'
    # print(txt)
    xsrf = re.match('.*name="_xsrf" value="(.*?)"',txt,re.S)
    if xsrf:
        xsrf= xsrf.group(1)
    print(xsrf)

    return xsrf

if __name__=="__main__":
    ssl._create_default_https_context = ssl._create_unverified_context

    opener=get_opener(heads)
    url="https://www.zhihu.com/"
    op=opener.open(url)
    data1=op.read()
    data1=ungzip(data1).decode('utf-8')
    #print(data1.decode('utf-8'))
    #print(op.read().decode('utf-8'))
##    xsrf=re.findall(r'name="_xsrf" value=".*"',data1)
##    print(xsrf[0])
##    print(type(xsrf[0]))
##    value=xsrf[0].split(" ")
##    print(value)
##    _xsrf=re.findall(r'".*"',value[1])[0]
##    print(_xsrf)
    # soup=BeautifulSoup(data1,"html.parser")
    # _xsrf=soup.find("input",{'type':'hidden'}).get("value")
    password="hzc19911005"
    #captcha_type="cn"
    phone_num="13267243809"
    captcha_url="https://www.zhihu.com/captcha.gif?r=%d&type=login"% (time.time() * 1000)
    captchadata=opener.open(captcha_url).read()
    with open("1.gif",'wb') as file:
        file.write(captchadata)
    yanzhengma=input("captcha:")
    postdata={
        "_xsrf":get_xsrf(),
        "password":password,
        #"captcha_type":captcha_type,#不能带有这个字段
        "phone_num":phone_num,
        "captcha":yanzhengma
        }
    postdata=urllib.parse.urlencode(postdata).encode()
    login_url="https://www.zhihu.com/login/phone_num"
    op2=opener.open(login_url,postdata)
    login_data=op2.read()
    data=ungzip(login_data).decode("utf-8")
    print(data)
    result=dict(eval(data))
    if result["r"]==0:
        print("登录成功")