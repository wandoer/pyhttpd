# -*- encoding:utf-8 -*-
# Author:   zrking
# Blog:     http://www.wandoer.com
# Email:    web@wandoer.com
# Date:     2016/11/20

'''
url映射

将请求的url映射到view及template
'''

import view 

class urlidx:
    def __init__(self,fun,template = ''):
        self.fun = fun
        self.template = template

    def getFun(self):
        return self.fun
    
    def getTemplate(self):
        return self.template

temppath = './template/'

urlMapper = {
    '/':            urlidx(view.index,temppath + 'index.html'),
    '/index/':       urlidx(view.index,temppath + 'index.html'),
    '/index.html/':  urlidx(view.index,temppath + 'index.html'),
    '/welcome.html': urlidx(view.welcome,temppath + 'welcome.html'),
    '/testpost.html':urlidx(view.testpost,temppath + 'testpost.html')
}