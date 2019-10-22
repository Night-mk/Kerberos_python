#!/usr/bin/python
# -*- coding: UTF-8 -*-
import hashlib

import collections
import datetime
import secrets
import logging
from Kerberos.body import *
from Kerberos.ID import *
from Kerberos.RC4 import *
import socket# 客户端 发送一个数据，再接收一个数据


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #声明socket类型，同时生成链接对象
client.connect(('localhost',100)) #建立一个链接，连接到本地的6969端口
#addr = client.accept()
#print ('连接地址：', addr)
print('输入用户名：')
msg=input()
print('输入密码:')
pw=input()
print('输入密码:')
pw=input()
print('输入密码:')
pw=input()
client.send(msg.encode('utf-8'))  #发送一条信息 python3 只接收btye流
client.send(pw.encode('utf-8'))
print('发送至AS')
data = client.recv(4096) #接收一个信息，并指定接收的大小 为1024字节
print('recv:',data.decode('utf-8')) #输出我接收的信息
client.close() #关闭这个链接
print('end')