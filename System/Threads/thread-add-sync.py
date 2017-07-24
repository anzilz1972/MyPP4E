#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-24 10:28:24
# @Author  : 王国安 
# @email   : 18909311025@189.cn 
# @Version : 1.0

"""
  对简单的全局变量count加锁进行访问
"""
import threading,time
count = 0

class Mythread(threading.Thread):
	def __init__(self,mutex):
		self.mutex = mutex
		threading.Thread.__init__(self)

	def run(self):
		global count;
		with self.mutex:count += 1
		time.sleep(2)
		with self.mutex:count += 1

addmutex = threading.Lock()
threads = []
for i in range(1000):
	thread = Mythread(addmutex)
	thread.start()
	threads.append(thread)

for thread in threads:thread.join()
print(count)

