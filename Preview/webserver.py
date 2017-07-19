#coding=utf-8
'''
Created on 2017年6月9日
@author: 王国安
用Python实现一个HTTP Web服务器，它知道如何运行服务器端CGI脚本；
从当前工作目录中提供文件和脚本；Python脚本必须存储在 webdir\cgi-bin或webdir\htbin中
'''
import os,sys
from http.server import HTTPServer,CGIHTTPRequestHandler

webdir = '.'    #存放HTML文件和cgi-bin脚本文件夹的所在   
port   = 80     #缺省http://localhost/,也可以使用http://localhost:xxxx/

os.chdir(webdir)
srvraddr = ('', port)
srvrobj  = HTTPServer(srvraddr,CGIHTTPRequestHandler)
srvrobj.serve_forever() 
