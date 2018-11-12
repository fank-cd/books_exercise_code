# coding:utf-8

from socket import *
from time import ctime

HOST = "localhost"
PORT = 21567
BUFSIZ = 1024  # 缓冲区大小
ADDR = (HOST, PORT)

udpClisock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input(">")
    if not data:
        break
    udpClisock.sendto(data, ADDR)
    data, ADDR = udpClisock.recvfrom(BUFSIZ)
    if not data:
        break
    print data

udpClisock.close()