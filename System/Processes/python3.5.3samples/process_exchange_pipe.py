#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-27 15:41:06
# @Author  : 王国安 
# @email   : 18909311025@189.cn 
# @Version : 1.0

"""
  1、摘自python-3.5.3-docs-html/library/multiprocessing.html的代码片段
  2、演示：
      1、use pipe,Exchanging objects between processes
      2、The Pipe() function returns a pair of connection objects 
         connected by a pipe which by default is duplex (two-way).
"""

from multiprocessing import Process,Pipe
import time


def f(conn):
	for i in range(5):
		conn.send([42,None,'hello, python'])
	print('Child process exit.')

if __name__ == '__main__':
	parent_conn,child_conn = Pipe()
	p = Process(target = f, args = (child_conn,))
	p.start()

	time.sleep(2)
	while True:
		#value = parent_conn.poll()
		#print('poll result:',value)
		if parent_conn.poll() == True:
			msg = parent_conn.recv()
			print(msg)
		else:
			break

	p.join()
	parent_conn.close()
	child_conn.close()
	print('Parent process exit.')
	

