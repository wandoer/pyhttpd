# -*- encoding:utf-8 -*-
# Author:   zrking
# Blog:     http://www.wandoer.com
# Email:    web@wandoer.com
# Date:     2016/11/20

'''
视图渲染

此模块用于定义渲染的方法，返回 response
'''

import render
import request

def index(request,template):
    rd = render.render(request,None, template)
    return rd.rend()

def welcome(request,template):
    if 'name' not in request.getParams():
        return render.render.rendInnerPage(request,400,None)
    else:
        rd = render.render(request,None,template)
        return rd.rend()

def testpost(request,template):
    print request.getParams()
    rd = render.render(request,None, template)
    return rd.rend()