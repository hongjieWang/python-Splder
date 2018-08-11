# -*- coding:utf-8 -*-
'''
使用代理访问百度
'''

from urllib import request,error
import ssl

if __name__ == '__main__':

    url = "http://www.baidu.com/"

    # 设置代理地址
    proxy = {'http': '120.194.18.90:81'}
    # 创建ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    # 创建Opener
    opener = request.build_opener(proxy_handler)
    # 安装Opener
    request.install_opener(opener)

    context = ssl._create_unverified_context()
    try:
        rsp = request.urlopen(url, context=context)

        html = rsp.read().decode()

        print(html)

    except error.URLError as e:
        print("URLError {0}".format(e.reason))
        print("URLError {0}".format(e))
    except error.HTTPError as e:
        print("HTTPError {0}".format(e.reason))
        print("HTTPError {0}".format(e))
    except Exception as e:
        print(e)
