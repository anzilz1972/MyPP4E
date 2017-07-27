#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-27 09:15:36
# @Author  : 王国安 
# @email   : 18909311025@189.cn 
# @Version : 1.0
"""
	a test of threading.Barrier object
	1、introduce:
	   Barrier，栅栏。 
	   栅栏，用来阻挡线程。栅栏有个栅栏强度，为一个数值，当被阻挡的线程达到栅栏强度时，栅栏被冲破，所有被栅栏阻挡的线程运行。
	2、use of Barrier
	   1)Barrier的使用，也比较简单，哪个线程调用Barrier的wait函数，哪个线程就被阻挡在栅栏外。
	   2)当栅栏被冲破之后，可手动恢复栅栏，继续阻挡下一次前来的线程。
	3、本程序中，并发线程只冲破栅栏一次

"""
import threading,time,random,sys

sys.path.append('..\..\others\log')						#将log模块加入到系统目录中
from MyPP4E_Log import Mypp4elog
logger = Mypp4elog()									#get logger object

numthread = 15

def fun():
	#线程启动后，随机等待N（N<=20）秒,之后被栅栏（Barrier）阻挡，等待其他线程
	tname = threading.currentThread().getName() 
	logger.debug('{} will have a rest!'.format(tname))
	duration = random.randint(1,20)
	time.sleep(duration)
	b.wait()
	logger.debug('{} has sleep {} seconds, now Exit.'.format(tname,duration))


if __name__ == '__main__':

	b = threading.Barrier(numthread)

	threads = []
	for i in range(numthread):
		thread = threading.Thread(target = fun, args = ())
		thread.start()
		threads.append(thread)

	for thread in threads:	thread.join()
	logger.debug('Main thread Exit.')










