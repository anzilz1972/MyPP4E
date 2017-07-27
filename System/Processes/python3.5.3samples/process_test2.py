#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-27 15:11:32
# @Author  : 王国安 
# @email   : 18909311025@189.cn 
# @Version : 1.0
"""
  1、摘自python-3.5.3-docs-html/library/multiprocessing.html的代码片段
  2、演示：生成子进程，打印父进程、子进程相关信息
"""

from multiprocessing import Process
import os

def info(title):
	print(title)
	print('module name:', __name__)
	print('parent process:', os.getppid())
	print('process id:',os.getpid())

def f(name):
	info('function f')
	print('hello, ', name)

if __name__ == '__main__':
	info('main line')
	p = Process(target = f, args = ('Python',))
	p.start()
	p.join()



