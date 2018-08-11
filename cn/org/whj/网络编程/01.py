# -*- coding:utf-8 -*-
"""
Server段流程
1、建立socket
2、
3、
4、
"""

import socket


def serverFunc():
    # 1、建立socket
    # socket.AF_INET ：使用IPv4协议族
    # socket.SOCK_DGRAM： 使用UDP通信
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2、绑定IP的端口
    # 地址是一个tuple类
    address = ("127.0.0.1", 8989)
    sock.bind(address)

    # 3\接收对方消息
    # 等待方式为死等
    # recvfrom接收的返回值是一个tuple，前一项表示数据，后一项表示地址
    # 参数的含义是缓冲区大小

    data, address = sock.recvfrom(500)

    print(data)
    print(type(data))

    # 4\发送过来的数据是bytes格式，必须通过解码才能得到str格式
    # decode默认解码格式utf-8
    text = data.decode()

    print(text)
    print(type(text))

    # 返回消息

    req = "I am not wtt"

    # 发送消息 默认编码utf-8
    data = req.encode()

    sock.sendto(data, address)


if __name__ == '__main__':
    print("Starting Server ....")
    serverFunc()
    print("Start SUEESS!")
