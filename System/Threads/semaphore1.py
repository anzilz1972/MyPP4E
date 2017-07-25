#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-25 09:51:52
# @Author  : 王国安 
# @email   : 18909311025@189.cn 
# @Version : 1.0

"""
  1、测试threading.Semaphore 
"""

import threading,time

numthreads = 10
semaphore = threading.Semaphore(2)
stdoutMutex = threading.Lock()



def fun():
	#每个线程标准动作：
	#请求信号量——》休眠2秒——》释放信号量——》退出
	threadName = threading.currentThread().getName()

	with stdoutMutex:
		print('{} waiting semaphore'.format(threadName))

	semaphore.acquire()
	with stdoutMutex:
		print('{} had got semaphore'.format(threadName))

	time.sleep(2)

	with stdoutMutex:
		print('{} release semaphore'.format(threadName))
	semaphore.release()

	with stdoutMutex:
		print('{} Exit.'.format(threadName))



if __name__ == '__main__':

	threads = []
	for i in range(numthreads):
		thread = threading.Thread(target = fun, name = 'Thread-{}'.format(i+1))   
		thread.start()
		threads.append(thread)

	for thread in threads:thread.join()   #主线程等待所有子线程完成之后退出

	print('Main thread Exit.')

