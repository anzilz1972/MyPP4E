#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-27 15:51:33
# @Author  : 王国安 
# @email   : 18909311025@189.cn 
# @Version : $Id$

"""
  1、摘自python-3.5.3-docs-html/library/multiprocessing.html的代码片段
  2、演示：
      1、use multiprocessing.Lock,Synchronization between processes 
"""

from multiprocessing import Process,Lock

def f(l,i):
	with l:
		print('hello world ',i)

if __name__ == '__main__':
	lock = Lock()
	for num in range(20):
		Process(target = f, args =(lock,num,)).start()

