# -*- coding:utf-8 -*-

from urllib import request
import ssl
import chardet

if __name__ == '__main__':
    url = "https://jobs.zhaopin.com/189130321250409.htm"
    context = ssl._create_unverified_context()
    rsp = request.urlopen(url, context=context)
    html = rsp.read()
    print(type(html))
    # 使用chardet自动检测页面编码
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)
    # 使用get保证不会出错，如果取不到值，默认utf-8
    html = html.decode(cs.get("encoding", "utf-8"))
    print(html)
