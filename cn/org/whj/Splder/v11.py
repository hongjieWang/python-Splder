# -*- coding:utf-8 -*-
'''
破解有道词典
'''

import time, random, hashlib
from urllib import request, error, parse

# 由js源码可知 salt 算法
# i = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10)),
# 翻译成python实现
from urllib.request import Request


def getSalt():
    # time.time()单位为s ,(new Date).getTime() 单位毫秒
    salt = int(time.time() * 1000) + random.randint(0, 10)
    return salt


def getMD5(key):
    md5 = hashlib.md5()
    md5.update(key.encode("utf-8"))
    sign2 = md5.hexdigest()
    return sign2


# 获取sign
# o = n.md5("fanyideskweb" + t + i + "ebSeFb%=XZ%T[KZ)c(sy!");
def getSign(v, salt):
    sign2 = "fanyideskweb" + v + str(salt) + "ebSeFb%=XZ%T[KZ)c(sy!"
    sign2 = getMD5(sign2)
    return sign2


def getPost(value):
    # 有道云URL
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    salt = getSalt()

    # 请求data
    data = {
        "i": value,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": str(salt),
        "sign": getSign(value, salt),
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }
    # 参数data需要是bytes格式 否则报 a bytes-like object is required, not 'str'
    data = parse.urlencode(data).encode()
    # headers
    headers = {
        "Accept": "application/json,text/javascript, */*;q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": len(data),
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "NTES_SESS=aicZo3tvJTD_jFRCW4QvC8bbDCW3W3aQM9Jes2H3KK8Y490e4zw3CZBxznQzS9RbDFA7vo3QZnaBGtI2vicJGmtaMdzEYzWPy3fSVsTXv24Sy6DoC94zuxGUTXphXINq0329Jo78wmfxVtEcVOubxoWE8JGWrgdPJTp8XMEgK5rofjBxstkOUcLcXP6Qpi44AhIZkrclPQ564bjt3M5yz3S8g; ANTICSRF=9cd36a130117688b76eec98667b81e42; S_INFO=1533824632|0|3&80##|julywhj; P_INFO=julywhj@163.com|1533824632|0|other|11&12|bej&1533811267&other#bej&null#10#0#0|182068&0||julywhj@163.com; OUTFOX_SEARCH_USER_ID=-622851639@10.168.8.76; JSESSIONID=aaaeegEGe2AL2hCez7Nuw; OUTFOX_SEARCH_USER_ID_NCOO=288396918.7876193; ___rl__test__cookies=1533977025972",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": " Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    try:
        req: Request = request.Request(url=url, data=data, headers=headers)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print("HttpError: {0} ".format(e.reason))
        print("HttpError: {0} ".format(e))
    except error.URLError as e:
        print("URLError: {0} ".format(e.reason))
        print("URLError: {0} ".format(e))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    getPost("python 系列项目，包括 爬虫，基础信息，强化学习")
