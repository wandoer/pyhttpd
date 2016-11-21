# -*- encoding:utf-8 -*-
# Author:   zrking
# Blog:     http://www.wandoer.com
# Email:    web@wandoer.com
# Date:     2016/11/20

'''
Http request
'''

import io

class request:
    METHOD = ['GET','POST']

    def __init__(self,data):
        self.__params = {}
        self.__initdata(data)
        

    def __initdata(self,data):
        if data == None or len(data) <=3 or (' ' not in data) :
            raise ValueError("Not a request data",data)
        
        line = ''
        idx = 0
        c = data[idx]
        while c != '\n':
            line = line + c
            idx = idx + 1
            c = data[idx]
        
        arr = line.split(' ')
        if len(arr) < 3:
            raise ValueError("Not a request dataline",line)

        if arr[0] not in request.METHOD:
            raise NotImplementedError("no implament method",arr[0])
        
        self.__method = arr[0]
        self.__httpVersion = arr[2]

        if arr[0] == 'GET':
            self.__initGETparams(arr[1])
        elif arr[0] == 'POST':
            self.__initPOSTparams(arr[1],data)
    
    def __initGETparams(self,uri):
        if '?' in uri:
            arr = uri.split('?')
            self.__uri = arr[0]
            if len(arr) > 1:
                params = arr[1].split('&')
                for p in params:
                    par = p.split('=')
                    if len(par) != 2:
                        continue
                    self.__params[par[0]] = par[1]
        else:
            self.__uri = uri

    def __initPOSTparams(self,uri,data):
        self.__uri = uri
        f = io.StringIO(unicode(data))
        line = f.readline()
        while True:
            if (line == '\r\n') or (len(line) == 0):
                break
            line = f.readline()
        
        if not line:
            return 
        
        line = f.readline()
        while line:
            params = []
            if '&' in line:
                params.append(line.split('&'))
            else:
                params.append(line)
            for p in params:
                par  = p.split('=')
                if len(par) != 2:
                    continue
                self.__params[par[0]] = par[1]
            line = f.readline()


    def getMethod(self):
        """
        方法
        """
        return self.__method

    def getHttpVersion(self):
        """
        Http 版本
        """
        return self.__httpVersion

    def getURI(self):
        """
        uri
        """
        return self.__uri
    
    def getParams(self):
        """
        参数(字典)
        """
        return self.__params