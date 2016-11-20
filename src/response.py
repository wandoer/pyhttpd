# -*- encoding:utf-8 -*-
# Author:   zrking
# Blog:     http://www.wandoer.com
# Email:    web@wandoer.com
# Date:     2016/11/20

'''
http response
'''

from time import ctime

RESPONSE_STATUS = {
    200:'OK',
    400:'Params error',
    404:'Not Found',
    500:'InternalServerError'
    } #定义状态码及状态描述

class Response:
    def __init__(self,status = 200,body=''):
        self.__status = status
        self.__body = body

    def setStatus(self,status):
        """
        设置状态
        """
        self.__status = status
    
    def setBody(self,body):
        """
        设置消息体
        """
        self.__body = body

    def getResponse(self):
        """
        获取 Response
        """
        buf = self.__getStatusLine()
        buf = buf + self.__getCommonHeader()
        buf = buf + '\r\n'
        buf = buf + self.__body
        return buf

    def __getCommonHeader(self):
        """获取通用的 Response 头 (已带CRLF).
        """
        buf = 'Date:' + ctime() + '\r\n'
        buf = buf + 'Server:pyHttpd\r\n'
        buf = buf + 'Content-Type:text/html\r\n'
        return buf

    def __getStatusLine(self):
        """获取 Response 状态行(已带CRLF).
        """
        httpVer = 'HTTP/1.1'
        return httpVer + ' ' + str(self.__status) + ' ' + RESPONSE_STATUS[self.__status] + '\r\n'