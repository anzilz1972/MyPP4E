#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-16 15:59:54
# @Author  : 王国安 
# @email   : 18909311025@189.cn 
# @Version : $Id$

"""
可创建Process类的子类，就像threading.Thread一样；Queue和queue.Queue
的使用方法类似，不过它不是线程间的工具，而是进程间的工具
"""

import os,time,queue
from multiprocessing import Process,Queue

class Counter(Process):
	label = ' @'
	def __init__(self,start,queue):
		self.state = start
		self.post  = queue
		Process.__init__(self)

	def run(self):
		for i in range(3):
			time.sleep(1)
			self.state += 1
			print(self.label,self.pid,self.state)
			self.post.put([self.pid,self.state])
		print(self.label,self.pid,'-')

if __name__ == '__main__':
	print('start',os.getpid())

	post = Queue()
	p1 = Counter(0,post)
	p2 = Counter(100,post)
	p3 = Counter(1000,post)

	p1.start();p2.start();p3.start()

	expected = 9
	while expected:
		time.sleep(0.5)
		try:
			data = post.get(block = False)
		except queue.Empty:
			print('no data...')
		else:
			print('posted:',data)
			expected -= 1

	p1.join();p2.join();p3.join()
	print('finish',os.getpid(),p3.exitcode)




