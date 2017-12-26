#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""

from socket import *

HOST = "127.0.0.1"
PORT = 11112
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input("> ")
    if not data:
        break
    # 编码后才能发送
    tcpCliSock.send(data.encode("utf-8"))
    # 接收后必须先解码
    data = tcpCliSock.recv(BUFSIZE).decode("utf-8")
    if not data:
        break
    print(data)

tcpCliSock.close()
