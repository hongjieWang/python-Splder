# -*- coding:utf-8 -*-

from urllib import request, error, parse
from http import cookiejar
import ssl

# 创建cookieJar实例
cookie = cookiejar.CookieJar()

# 生成 cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)

# 创建http请求管理器
http_handler = request.HTTPHandler()

# 生成https管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)

ssl._create_default_https_context = ssl._create_unverified_context


def login():
    """
    负责初次登陆
    需要输入用户名密码，用来获取登录cookie凭证
    :return:
    """
    print("----")
    url = "https://passport.csdn.net/account/verify"

    # 模拟请求参数
    data = {
        'username': '18232533068',
        'password': '125846Whj1993'
    }

    # data 进行编码
    data = parse.urlencode(data).encode()

    # 创建一个请求对象
    req = request.Request(url=url, data=data)

    # 使用opener发起请求
    rsp = opener.open(req)

    html = rsp.read().decode()

    with open("login.html", 'w') as f:
        f.write(html)


def getHomePage():
    url = "https://my.csdn.net/"

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

    req = request.Request(url=url, headers=headers)
    # 如果已经执行了login函数，则opener自动已经包含相应的cookie
    rsp = opener.open(req)

    html = rsp.read().decode()
    print(html)
    with open("rsp.html", 'w') as f:
        f.write(html)


if __name__ == '__main__':
    login()
    getHomePage()
