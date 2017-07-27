#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-27 15:30:38
# @Author  : 王国安 
# @email   : 18909311025@189.cn 
# @Version : $Id$

"""
  1、摘自python-3.5.3-docs-html/library/multiprocessing.html的代码片段
  2、演示：
      1)使用contex对象，代替multiprocessing模块
        Alternatively, you can use get_context() to obtain a context object. 
        Context objects have the same API as the multiprocessing module, 
        and allow one to use multiple start methods in the same program.
      2)在context对象中确定子进程启动模式,windows platform, 'spawn' is only start mode
"""
import multiprocessing as mp

def foo(q):
	q.put('hello, python!')

if __name__ == '__main__':
	ctx = mp.get_context('spawn')              #windows platform, 'spawn' is only start mode
	q = ctx.Queue()
	p = ctx.Process(target = foo, args = (q,))
	p.start()
	print(q.get())
	p.join()

