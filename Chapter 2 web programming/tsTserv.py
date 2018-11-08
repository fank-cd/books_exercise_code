# coding:utf-8
from socket import *
from time import ctime

HOST = ""
PORT = 21567
BUFSIZ = 1024  # 缓冲区大小
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)  # AF_INET:网络编程 SOCK_STREAM:TCP
tcpSerSock.bind(ADDR)  # 绑定地址
tcpSerSock.listen(5)  # 最大连接请求数
while True:
    print "waitting for connection"
    tcpCliSock,addr = tcpSerSock.accept()
    print "...connected from:", addr

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send('[%s] %s' % (ctime(), data))
    print "shut down from :", addr
    tcpCliSock.close()

tcpSerSock.close()  #这并不会被调用，但是可以提醒我们随时想着优雅地关闭这件事情