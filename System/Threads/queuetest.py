#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-24 10:50:08
# @Author  : 王国安 
# @email   : 18909311025@189.cn 
# @Version : 1.0

"""生产者和消费者线程与共享队列进行通信"""
import _thread as thread,queue,time

numconsumers = 3                                        #消费线程数量
numproducers = 4                                        #生产线程数量
nummessages  = 4                                        #每个生产者存入队列的消息的数量

stdoutmutex = thread.allocate_lock()                    #标准输出锁，避免打印错误
dataQueue = queue.Queue()

def producer(id):
	for msgnum in range(nummessages):
		time.sleep(id)
		dataQueue.put('[producer id = {},count = {}]'.format(id,msgnum+1))

def consumer(id):
	processcounts = 0
	while True:
		time.sleep(0.1)
		try:
			data = dataQueue.get(block = False)
		except queue.Empty:
			pass
		else:
			processcounts += 1
			with stdoutmutex:
				print('consumer {} got => {},total {} times!'.format(id,data,processcounts))


if __name__ =='__main__':
	for i in range(1,numconsumers+1):
		thread.start_new_thread(consumer,(i,))
	for i in range(1,numproducers+1):
		thread.start_new_thread(producer,(i,))
	time.sleep(((numproducers -1) * nummessages) +1)
	print('Main thread exit.')






