#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""
from socket import *
from time import ctime

HOST = ""
PORT = 11112
BUFFERSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print("waiting for connection...")
    tcpCliSock, addr = tcpSerSock.accept()
    print("...connected from:", addr)

    while True:
        # 接受后必须先解码
        data = tcpCliSock.recv(BUFFERSIZE).decode("utf-8")
        if not data:
            break
        # 字符串编码后才能发送
        tcpCliSock.send(("[%s] %s" % (ctime(), data)).encode("utf-8"))
        
    tcpCliSock.close()
tcpSerSock.close()

