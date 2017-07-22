#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-22 21:08:12
# @Author  : wangguoan
# @eMail   : 18909311025@189.cn
# @Link    : http://example.org
# @Version : 1.0

"""
使用简单的共享全局数据（不是mutextes）在主线程中
探知子线程何时结束；线程共享列表但不共享列表里的
对象，假设列表在内存中创建后不会移动
"""

import _thread as thread

numthreads  = 10
timescounter= 0 
stdoutmutex = thread.allocate_lock()
exitmutexes = [False] * numthreads

def counter(myId,count):
	global timescounter
	for i in range(count):
		stdoutmutex.acquire()
		print('thread id:{} => {}'.format(myId,i))
		timescounter += 1
		stdoutmutex.release()
	exitmutexes[myId] = True

for i in range(numthreads):
	thread.start_new_thread(counter,(i,100))

while False in exitmutexes:pass
print('Total {} counter！Main thread exiting.'.format(timescounter))



