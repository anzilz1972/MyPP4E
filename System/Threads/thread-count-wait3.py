#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-22 21:22:39
# @Author  : wangguoan
# @eMail   : 18909311025@189.cn
# @Link    : http://example.org
# @Version : 1.0

"""
传入所有线程共享的mutex对象而非全局对象；和上下文管理器
语句一起使用，实现所得自动获取/释放；添加休眠功能的调用
以避免繁忙的循环并模拟真实工作
"""

import _thread as thread,time

numthreads  = 10
timescounter= 0 
stdoutmutex = thread.allocate_lock()
exitmutexes = [thread.allocate_lock() for i in range(numthreads)]

def counter(myId,count,mutex):
	global timescounter
	for i in range(count):
		time.sleep(1/(myId+1))
		with mutex:
			print('thread id:{} => {}'.format(myId,i))
			timescounter += 1
	exitmutexes[myId].acquire()

for i in range(numthreads):
	thread.start_new_thread(counter,(i,5,stdoutmutex))

while not all(mutex.locked() for mutex in exitmutexes):time.sleep(0.25)
print('Total {} counter！Main thread exiting.'.format(timescounter))






