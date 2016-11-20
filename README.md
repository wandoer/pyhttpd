# pyHttpd #
a simple httpserver by python
##简介##
pyHttpd 是一款采用 Python 开发的简单的 HTTPServer。  
其有以下特点：     
- 简单。使用最常用的 Python 语法实现 C/S 端的 Request/Response传输。     
- 清析。使用面向对象思想将 HTTP 协议的各个部分模块化。 将 HTTP 协议部分与数据部分分开处理。  

##使用##
1. 在 template 建立页面模板模板中使用 ${param_name} 来建立占用符
2. 在 src/view 中添加方法对象用于处理 Request，并返回 Response .可以借助 src/render 模块，将request（主要是request中的参数）或自定义的参数(字典)传入 render 来快速生成 response。
3. 在 src/url 的 urlMapper 中添加 URL 映射。将 URL 映射到第 2 步的方法对象和第一步的模板名称中
4. 在 pyhttpd.py 中配置好 HOST,PORT 后运行运行此文件，即可启动服务器




----------
## 日志 ##
### 2016/11/20 ###
**V0.1** 


1. 其于单线程的 TCP 实现简单的 GET Request 处理。
2. 简单的 MVC 模块化。实现基本的 HTML 模板渲染。实现 200/400/404/500 等状态的 Response 
3. 实现 URL 映射


