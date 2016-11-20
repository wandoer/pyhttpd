# -*- encoding:utf- -*-

# Author:   zrking
# Blog:     http://www.wandoer.com
# Email:    web@wandoer.com
# Date:     2016/11/20
#version:	v0.1
#remark:	简单实现 http 服务器，用于学习 HTTP 协议。更多内容请访问 http://wandoer.com/coding/networks_protocol_http.htm
#

import os
from socket import *
from time import ctime
from src import request
from src import response
from src.url import urlMapper
#from src import view
from src.view import *


def sendResponse(skt, rsps):
	if rsps != None:
		print rsps.getResponse()
		skt.send(rsps.getResponse())
	else:
		return


def getResponse(data):
	try:
		rqst = request.request(data)
		uri = rqst.getURI()
		uidx = urlMapper[uri]
		if uidx != None:
			return uidx.getFun()(rqst,uidx.getTemplate())
	except ValueError,e:
		print e
		return None
	except NotImplementedError,e:
		print e
		return None
	except Exception,e:
		print e
		return None
		

#======================== config =====================

HOST = '127.0.0.1'  	#服务器地址
PORT = 9891				#服务端端口
BUFSZ = 10240			#支持最大 Request 长度
		
STATICPATH = './template/'	#静态资源路径

STATUS_CODE = {200:'OK',404:'Not Found',500:'InternalServerError'} #定义状态码及状态描述

#======================= main =======================

ADDR = (HOST,PORT)
skt = socket(AF_INET,SOCK_STREAM)		#建立socket
skt.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)	#设置地址复用
skt.bind(ADDR)	#绑定地址

skt.listen(5)

while True:
	tcpClientSkt,addr = skt.accept()
	print 'accept from [%s,%s]' % (str(addr[0]),str(addr[1]))
	while True:
		try:
			data = tcpClientSkt.recv(BUFSZ)
		except Exception,e:
			print 'Exception',e
			tcpClientSkt.close()
			break
		if not data:
			break
		msg = '[%s] :\r\n%s' % (ctime(),data)
		print msg

		rsps = getResponse(data)

		sendResponse(tcpClientSkt,rsps)

		tcpClientSkt.close()
skt.close()
