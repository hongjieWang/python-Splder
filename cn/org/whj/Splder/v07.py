# -*- coding:utf-8 -*-
'''
UA
访问一个网站
更改自己的UA进行伪装
'''

from urllib import request, error
import ssl

if __name__ == '__main__':

    url = 'http://www.baidu.com'

    try:
        # 使用heads伪装UA
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
        context = ssl._create_unverified_context()
        req = request.Request(url, headers=headers)

        # 正常访问
        rsp = request.urlopen(req, context=context)
        html = rsp.read().decode()
        print(html)

    except error.HTTPError as e:
        print("HttpError: {0}".format(e.reason))
        print("HttpError: {0}".format(e))
    except error.URLError as e:
        print("URLError: {0}".format(e.reason))
        print("URLError: {0}".format(e))
    except Exception as e:
        print(e)
