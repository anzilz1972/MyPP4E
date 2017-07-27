#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-27 17:30:35
# @Author  : 王国安 
# @email   : 18909311025@189.cn 
# @Version : 1.0

"""
  1、摘自python-3.5.3-docs-html/library/multiprocessing.html的代码片段
  2、演示：
      Sharing state between processes,method one:use Server process
      1)As mentioned above, when doing concurrent programming it is usually best to avoid using shared state as far as possible. This is particularly true when using multiple processes.
	  However, if you really do need to use some shared data then multiprocessing provides a couple of ways of doing so.
	  2)A manager object returned by Manager() controls a server process which holds Python objects and allows other processes to manipulate them using proxies.
	    Manager()函数产生的manager对象可以控制一个server process(服务进程),此服务进程拥有Python对象；manager对象允许其他进程使用代理来修改服务进程的python对象
"""

from multiprocessing import Process,Manager
from random import random,randint

def f(d,l):
	d[1] = randint(0,1000)
	d[2] = random()
	d[3] = random() * 100

	for i in range(len(l)):
		l[i] = random() * randint(0,10000)

if __name__ == '__main__':
	with Manager() as manager:
		d = manager.dict()
		l = manager.list(range(10))

		p = Process(target = f, args = (d,l))
		p.start()
		p.join()

		print(d)
		print(l)


