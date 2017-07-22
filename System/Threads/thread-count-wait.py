#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-22 17:48:13
# @Author  : wangguoan
# @eMail   : 18909311025@189.cn
# @Link    : http://example.org
# @Version : 1.0

"""
使用mutexts在父/主线程中探知子线程何时结束，而不再使用
time.sleep;给stdout加锁以避免混杂在一起的打印输出
"""

import _thread as thread

numthreads = 10
stdoutmutex = thread.allocate_lock()
exitmutexes = [thread.allocate_lock() for i in range(numthreads)]

timescounter = 0

def counter(myId,count):
	global timescounter
	for i in range(count):
		stdoutmutex.acquire()
		print('thread id:{} => {}'.format(myId,i))
		timescounter += 1
		stdoutmutex.release()
	exitmutexes[myId].acquire()  #加锁，用以向主线程发信号


for i in range(numthreads):
	thread.start_new_thread(counter,(i,100))

while not all(mutex.locked() for mutex in exitmutexes):pass

print('Total {} counter！Main thread exiting.'.format(timescounter))




