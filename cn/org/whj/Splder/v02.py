# -*- coding:utf-8 -*-

# get 方式访问百度

from urllib import request, parse

if __name__ == '__main__':
    url = 'http://www.baidu.com/s?'

    wd = input("请输入查询参数：")

    # 要想使用date 使用字典结构

    qs = {
        'wd': wd
    }

    # 转换url编码

    qs = parse.urlencode(qs)

    fullurl = url + qs

    print(fullurl)

    rsp = request.urlopen(fullurl)

    html = rsp.read()

    html = html.decode()

    print(html)

