# coding:utf-8

from socket import *
from time import ctime

HOST = ""
PORT = 21567
BUFSIZ = 1024  # 缓冲区大小
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)  # AF_INET:网络编程 SOCK_STREAM:UDP
udpSerSock.bind(ADDR)  # 绑定地址
# 因为是UDP 所以没有listen这个方法
while True:
    print "waitting for message"
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto("[%s] %s" % (ctime(), data), addr) # 面向无连接的，之前没有建立连接，所以这里会带上客户端的addr
    print "..recevied from and returned to :", addr

udpSerSock.close()