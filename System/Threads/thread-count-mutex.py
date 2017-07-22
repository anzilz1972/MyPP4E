#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-22 17:33:47
# @Author  : wangguoan
# @eMail   : 18909311025@189.cn
# @Link    : http://example.org
# @Version : 1.0

"""
同步对stdout的访问：因为stdout为共享的全局对象，
线程输出如果不做同步可能会交互混杂在一起
"""


import _thread as thread,time

def counter(myId,count):
	for i in range(count):
		time.sleep(1)
		mutex.acquire()
		print('thread id:{} => {} '.format(myId,i))
		mutex.release()

mutex = thread.allocate_lock()
for i in range(10):
	thread.start_new_thread(counter,(i,5))

#time.sleep(6)
while input() =='q':break
print('Main thread exiting.')
