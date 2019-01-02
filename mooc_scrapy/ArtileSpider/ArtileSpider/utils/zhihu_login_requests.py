# coding:utf-8
import requests

try:
    import cookielib

except:
    import http.cookiejar as cookielib

import re

session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename="cookies.txt")
try:
    session.cookies.load(ignore_discard=True)
except:
    print("cookie未能加载")

agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0"
header =  {
    "HOST": "www.zhihu.com",
    "Referer": "https://www.zhihu.com",
    "User-Agent":agent
}

def is_login():
    #通过个人中心页面返回状态码来判断是否为登录状态

    inbox_url = "https://www.zhihu.com/inbox"
    response = session.get(inbox_url, headers=header,allow_redirects=False)
    if response.status_code != 200:
        return False
    else:
        return True


def get_xsrf():

    # 获取xsrf
    response = session.get("https://www.zhihu.com", headers=header)

    text = '<input type="hidden" name="_xsrf" value="12b81b21b219069a5cb633c214f64726"'
    match_obj = re.match('.*name="_xsrf" value="(.*?)"', response.text)
    if match_obj:
        print(match_obj.groups())
    else:
        return ""


def get_index():
    response = session.get("https://www.zhihu.com", headers=header)
    with open("index_page.html","wb") as f:
        f.write(response.text.encode("utf-8"))
    print("OK")


def zhihu_login(account, password):

    if re.match("^1\d{10}", account):
        print("手机号码登录")
        post_url = "https://www.zhihu.com/login/phone_num"
        post_data = {
            "_xsrf": get_xsrf(),
            "phone_num": account,
            "password": password
        }


    else:
        if "@" in account:
            print("邮箱方式登录")
            post_url = "https://www.zhihu.com/login/email"
            post_data = {
                "_xsrf": get_xsrf(),
                "email": account,
                "password": password
            }
    response_text = session.post(post_url=post_url, data=post_data, headers=header)
    session.cookies.save()
# zhihu_login("acc","")
# get_xsrf()
get_index()

