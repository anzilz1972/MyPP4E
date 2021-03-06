#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-24 10:50:08
# @Author  : 王国安 
# @email   : 18909311025@189.cn 
# @Version : 1.0
"""
   1、在queuetest3.py基础上，学习logging模块
   2、不再使用stdoutMutex同步stdout输出，而是直接用logging.StreamHandler输出到stderr,此输出是线程安全的
"""
"""
   queuetest3.py：
   1、生产者和消费者线程与共享队列进行通信
   2、共享队列作为参数进行传递
   3、主线程等待生产者线程完成所有工作后，通知消费者线程退出
   4、线程生成时进行命名；线程名称在过程函数中使用
"""
import threading,queue,time,sys

sys.path.append('..\..\others\log')						#将log模块加入到系统目录中
from MyPP4E_Log import Mypp4elog
logger = Mypp4elog()									#get logger object

numconsumers = 3                                        #消费线程数量
numproducers = 100                                      #生产线程数量
nummessages  = 10                                       #每个生产者存入队列的消息的数量

dataQueue = queue.Queue()                               #共享队列
consumersExitflag = threading.Event()                   #消费者线程退出标志，由主线程设置


def producer(dataqueue):
	nameStr = threading.currentThread().getName()
	for msgnum in range(nummessages):
		time.sleep(0.01)
		dataqueue.put('[{},count = {}]'.format(nameStr,msgnum+1))
	logger.warning('{} Exit.'.format(nameStr))

def consumer(dataqueue):
	processcounts = 0
	nameStr = threading.currentThread().getName()
	while True:
		time.sleep(0.02)
		try:
			data = dataqueue.get(block = False)
		except queue.Empty:
			pass
		else:
			processcounts += 1
			logger.info(' {} got => {},total {} times!'.format(nameStr,data,processcounts))
		if consumersExitflag.isSet():break   #如果消费者线程退出标志被设置，则跳出循环
	logger.warning('{} Exit.'.format(nameStr))

			   
if __name__ =='__main__':
	consumersExitflag.clear()                     #初始化消费者线程退出标志为False
	
	for i in range(numconsumers):
		nameStr = 'Consumer{0:2}'.format(i)
		thread = threading.Thread(target = consumer,args = (dataQueue,),name = nameStr)
		thread.start()

	waitfor = []
	for i in range(numproducers):
		nameStr = 'Producer{0:2}'.format(i)
		thread = threading.Thread(target = producer,args = (dataQueue,),name = nameStr)
		waitfor.append(thread)
		thread.start()

	for thread in waitfor:thread.join()            #等待生产者线程全部结束
	while not dataQueue.empty():time.sleep(1)      #等待消费者线程处理完队列
	consumersExitflag.set()                        #设置消费者线程退出标志为真，通知消费者线程全部退出
	logger.warning('Main thread exit.')






