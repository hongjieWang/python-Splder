# -*- coding:utf-8 -*-

from urllib import request, parse
# 负责处理json
import json

'''
使用request实现
大概流程
1、利用data构造内容，然后URL open打开
2、返回一个json格式的数据
3、获取结果
'''

baseUrl = 'http://fanyi.baidu.com/sug'

data = input("请输入要翻译的词：")

data = {
    'kw': data
}

# 使用parse进行url编码
data = parse.urlencode(data).encode()

# 构造一个请求头，请求头至少包含请求数据的长度
# request要求传入的请求头是一个dict格式
headers = {
    # post请求至少应该包含 content-length字段
    'Content-Length': len(data)
}

# 构造一个request实例

req = request.Request(url=baseUrl, data=data, headers=headers)

# 因为已经构造了一个Request请求实例，则所有的信息都可以封装在Request实例中

# 发送请求
rsp = request.urlopen(req)

json_data = rsp.read().decode()

# print(json_data)

# 将json字符串转换成字典

json_data = json.loads(json_data)

# print(json_data)

for item in json_data['data']:
    print(item['k'], '---', item['v'])
