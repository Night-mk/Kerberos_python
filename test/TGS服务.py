#!/usr/bin/python
# -*- coding: UTF-8 -*-
import collections
import datetime
import secrets
import logging
import socket
from Kerberos.body import *
from Kerberos.ID import *
from Kerberos.RC4 import *
# 建立一个服务端
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',100)) #绑定要监听的端口
server.listen(5) #开始监听 表示可以使用五个链接排队
print('AS等待连接')
while True:# conn就是客户端链接过来而在服务端为期生成的一个链接实例
	conn,addr = server.accept() #等待链接,多个链接的时候就会出现问题,其实返回了两个值
	print(conn,addr)
	print('连接成功，接收数据')

	data1 = conn.recv(4096)  #接收数据
	data2 = conn.recv(4096)
	data3 = conn.recv(4096)  
	data4 = conn.recv(4096)
	print('recive:',data1.decode()) #打印接收到的数据
	print('Ticket_v生成成功，已发送')
	data=TGT.encode('utf-8')
	conn.send(data) #然后再发送数据
	print('AS等待连接')

'''except ConnectionResetError as e:
    print('关闭了正在占线的链接！')
    conn.close()'''