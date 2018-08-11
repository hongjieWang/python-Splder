# -*- coding:utf-8 -*-
"""
Server段流程
"""

import socket


def serverFunc():
    # 1、建立socket
    # socket.AF_INET ：使用IPv4协议族
    # socket.SOCK_DGRAM： 使用UDP通信
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2、绑定IP的端口
    # 地址是一个tuple类
    address = ("127.0.0.1", 8989)
    sock.bind(address)

    # 3、监听接入的访问socket
    sock.listen()

    while True:
        # 4、接收访问的socket
        # accept 返回的元祖第一个元素赋值给skt,第二个赋值给address
        skt, address = sock.accept()
        # 5、接收对方发送的消息，利用socket接收内容
        # 500代表接收使用的buffersize
        msg = skt.recv(500)
        # 接收到的是bytes格式内容
        # 想得到str格式的，需要进行解码
        msg = msg.decode()

        rst = "Received msg:{0} from {1}".format(msg, address)

        print(rst)

        # 6、如果有必要，给对方发送返回消息

        skt.send(rst.encode())
        # 7、关闭链接

        skt.close()


if __name__ == '__main__':
    print("Starting Server ....")
    serverFunc()
    print("Start SUEESS!")
