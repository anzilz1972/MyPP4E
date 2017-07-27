#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-27 15:23:30
# @Author  : 王国安 
# @email   : 18909311025@189.cn 
# @Version : 1.0
"""
  1、摘自python-3.5.3-docs-html/library/multiprocessing.html的代码片段
  2、演示：
        1)选择子进程启动模式,windows platform, 'spawn' is only start mode
        2)使用multiprocessing.Queue
"""
import multiprocessing as mp

def foo(q):
	q.put('hello, python!')

if __name__ == '__main__':
	mp.set_start_method('spawn')              #windows platform, 'spawn' is only start mode
	q = mp.Queue()
	p = mp.Process(target = foo, args = (q,))
	p.start()
	print(q.get())
	p.join()


