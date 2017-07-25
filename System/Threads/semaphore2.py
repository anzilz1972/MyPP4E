#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-25 10:42:36
# @Author  : 王国安 
# @email   : 18909311025@189.cn 
# @Version : 1.0

"""
	1、使用semaphore控制producer、consumer线程
"""

import threading,time,random

numthreads = 20                                         #Producer、consumer线程数量
semaphore = threading.Semaphore(0)                      #目前生产的items数量
stdoutMutex = threading.Lock()				            #stdout流锁
items = []	                                            #存储生产的item

def producer():
	global items
	threadName = threading.currentThread().getName()
	time.sleep(5)
	item = random.randint(1,10000)
	items.append(item)
	with stdoutMutex:
		print('{} produced item number {},exiting now.'.format(threadName,item))
	semaphore.release()


def consumer():
	global items
	threadName = threading.currentThread().getName()
	with stdoutMutex:
		print('{} is waiting.'.format(threadName))
	semaphore.acquire()
	with stdoutMutex:
		print('{} consumed item number {},exiting now.'.format(threadName,items.pop()))

if __name__ == '__main__':

	threads = []
	for i  in range(numthreads):
		thread = threading.Thread(target = consumer, name = 'Consumer{0:2}'.format(i+1))
		thread.start()
		threads.append(thread)

	for i  in range(numthreads):
		thread = threading.Thread(target = producer, name = 'Producer{0:2}'.format(i+1))
		thread.start()
		threads.append(thread)

	for thread in threads:thread.join()							#主线程等待所有线程结束后再退出
	print('Main thread Exit.')









