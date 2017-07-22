#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-22 21:41:03
# @Author  : wangguoan
# @eMail   : 18909311025@189.cn
# @Link    : http://example.org
# @Version : 1.0
"""
带有状态和run()行为的的线程类实例。
使用较高层面的类JAVA的threading模块对象连接方法
（而非mutexes或全局共享变量），在主线程中探知子线程结束时间
"""

import threading,time

class Mythread(threading.Thread):
	def __init__(self,myId,count,mutex):
		self.myId  = myId
		self.count = count
		self.mutex = mutex
		threading.Thread.__init__(self)

	def run(self):
		for i in range(self.count):
			with self.mutex:
				print('thread id:{} => {}'.format(self.myId,i))
				time.sleep(0.05)

numthreads  = 10
stdoutmutex = threading.Lock()
threads = []
for i in range(numthreads):
	thread = Mythread(i,100,stdoutmutex)
	thread.start()
	threads.append(thread)

for thread in threads:
	thread.join()    											#等待子线程退出
print('Main thread exiting.')






