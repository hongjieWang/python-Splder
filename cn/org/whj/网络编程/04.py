# -*- coding:utf-8 -*-

import socket

import serializers

def tcp_clt():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    address = ('127.0.0.1', 8989)

    sock.connect(address)

    msg = "djksajdaskd你撒的d"

    sock.send(msg.encode())

    ret = sock.recv(500)

    print(ret.decode())

    sock.close()


if __name__ == '__main__':
    serializers.serializer()
    tcp_clt()
