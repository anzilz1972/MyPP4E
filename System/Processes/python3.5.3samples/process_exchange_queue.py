#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-27 15:36:34
# @Author  : 王国安 
# @email   : 18909311025@189.cn 
# @Version : 1.0

"""
  1、摘自python-3.5.3-docs-html/library/multiprocessing.html的代码片段
  2、演示：
      use Queues,Exchanging objects between processes
"""

from multiprocessing import Process,Queue

def f(q):
	q.put([42,None,'hello, python'])

if __name__ == '__main__':
	q = Queue()
	p = Process(target = f, args = (q,))
	p.start()
	print(q.get())
	p.join()
	

