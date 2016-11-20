# -*- encoding:utf-8 -*-
# Author:   zrking
# Blog:     http://www.wandoer.com
# Email:    web@wandoer.com
# Date:     2016/11/20

'''
渲染

此模块使用请求参数对模板进行渲染，返回response
'''

import os
import response

class render:

    __INNER_PAGE = {
        400:"./innerpage/400.html",
        404:"./innerpage/404.html",
        500:"./innerpage/500.html"
    }

    @classmethod
    def rendInnerPage(cls,request,code,content):
        rsps = response.Response(code)
        bd = render.__getRawBody(render.__INNER_PAGE[code])
        return render.__rend(request,content,bd,rsps)

    def __init__(self,request,content = None,template = None):
       self.__content = content
       self.__template = template
       self.__request = request
       self.__response = response.Response()

    def rend(self):
        print 'rend--'
        if self.__template == None or self.__template == '' or os.path.exists(self.__template) == False:
            param = {}
            param['pageurl'] = self.__request.getURI()
            return render.rendInnerPage(request,404,param)
        else:
            rawbody = render.__getRawBody(self.__template)
            return render.__rend(self.__request,self.__content,rawbody,self.__response)

    @classmethod
    def __rend(cls,request,content,rawbody,response):
        print content
        if content != None:
            for ct in content.keys():
                pn = str('${' + ct + '}')
                print pn
                rawbody = rawbody.replace(pn,content[ct])
        for p in request.getParams().keys():
            pn = str('${' + p + '}')
            rawbody = rawbody.replace(pn,request.getParams()[p])
        response.setBody(rawbody)
        return response 

    @classmethod
    def __getRawBody(cls,path):
        f = open(path,'r')
        buf = f.read()
        f.close()
        return buf
