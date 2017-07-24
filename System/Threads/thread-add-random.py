#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-24 10:17:20
# @Author  : 王国安 
# @email   : 18909311025@189.cn 
# @Version : 1.0

"""
  如果对简单的全局变量count不做同步，在windows下每次运行时会打印不同的结果
"""

import threading,time
count = 0

class Mythread(threading.Thread):
	def run(self):
		global count;
		count += 1
		time.sleep(2)
		count += 1

threads = []
for i in range(1000):
	thread = Mythread()
	thread.start()
	threads.append(thread)

for thread in threads:thread.join()
print(count)




