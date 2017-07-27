#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-27 15:04:49
# @Author  : 王国安 
# @email   : 18909311025@189.cn 
# @Version : 1.0

"""
  1、摘自python-3.5.3-docs-html/library/multiprocessing.html的代码片段
  2、演示：生成子进程
"""


from multiprocessing import Process

def f(name):
	print('hello, ', name)

if __name__ == '__main__':
	p = Process(target = f, args = ('Python',))
	p.start()
	p.join()
