# -*- coding:utf-8 -*-

import socket


def clientFunc():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    text = "I LOve wtt"

    data = text.encode()

    sock.sendto(data, ('127.0.0.1', 8989))

    data, address = sock.recvfrom(200)

    data = data.decode()

    print(data)


if __name__ == '__main__':
    clientFunc()
