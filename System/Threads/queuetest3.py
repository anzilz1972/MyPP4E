#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-24 10:50:08
# @Author  : 王国安 
# @email   : 18909311025@189.cn 
# @Version : 1.0

"""
   1、生产者和消费者线程与共享队列进行通信
   2、共享队列作为参数进行传递
   3、主线程等待生产者线程完成所有工作后，通知消费者线程退出
"""
import threading,queue,time

numconsumers = 3                                        #消费线程数量
numproducers = 10                                       #生产线程数量
nummessages  = 10                                       #每个生产者存入队列的消息的数量

stdoutmutex = threading.Lock()                          #标准输出锁，避免打印错误
dataQueue = queue.Queue()
consumersExitflag = threading.Event()

def producer(id,dataqueue):
	for msgnum in range(nummessages):
		time.sleep(0.01)
		dataqueue.put('[producer id = {},count = {}]'.format(id,msgnum+1))
	with stdoutmutex:
		print('producer {} Exit.'.format(id))


def consumer(id,dataqueue):
	processcounts = 0
	while True:
		time.sleep(0.02)
		try:
			data = dataqueue.get(block = False)
		except queue.Empty:
			pass
		else:
			processcounts += 1
			with stdoutmutex:
				print('consumer {} got => {},total {} times!'.format(id,data,processcounts))
		if consumersExitflag.isSet():break   #如果退出标志为真，则跳出循环
	
	with stdoutmutex:
		print('consumer {} Exit.'.format(id))
			   
if __name__ =='__main__':
	consumersExitflag.clear()                     #初始化退出标志为False
	for i in range(1,numconsumers+1):
		thread = threading.Thread(target = consumer,args = (i,dataQueue))
		thread.start()

	waitfor = []
	for i in range(1,numproducers+1):
		thread = threading.Thread(target = producer,args = (i,dataQueue))
		waitfor.append(thread)
		thread.start()

	for thread in waitfor:thread.join()            #等待生产者线程全部结束
	while not dataQueue.empty():time.sleep(1)      #等待消费者线程处理完队列
	consumersExitflag.set()                         #通知消费者线程全部退出
	print('Main thread exit.')






