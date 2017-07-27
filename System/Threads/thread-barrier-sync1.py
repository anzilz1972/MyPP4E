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
	   1)哪个线程调用Barrier的wait函数，哪个线程就被阻挡在栅栏外。
	   2)当栅栏被冲破之后自动恢复，继续阻挡下一波线程。
	3、本程序中,栅栏被多次冲破

"""
import threading,time,random,sys

sys.path.append('..\..\others\log')						#将log模块加入到系统目录中
from MyPP4E_Log import Mypp4elog
logger = Mypp4elog()									#get logger object

numthread = 15											#线程数量上限
exitflag = threading.Event()							#所有线程退出标志
maxsleepseconds = 20									#线程最大休眠时间

def fun():
	tname = threading.currentThread().getName() 
	while True:
		#如果探测到主线程设置的退出标志，跳出循环
		if exitflag.isSet():break;

		#随机等待maxsleepseconds秒,之后被栅栏（Barrier）阻挡，等待其他线程
		duration = random.randint(1,maxsleepseconds)
		time.sleep(duration)
		logger.debug('{} is gathering at barrier!'.format(tname))

		try:		
			#最多被栅栏阻挡maxsleepseconds + 5秒
			b.wait(timeout = maxsleepseconds + 5)
		except threading.BrokenBarrierError:
			logger.warning('{} wait barrier timeout!'.format(tname))
		else:
			logger.debug('{} has escape from barrier!'.format(tname,duration))
	logger.debug('{} has detected exit flag,now Exit.'.format(tname))


if __name__ == '__main__':

	b = threading.Barrier(numthread-5)
	exitflag.clear()
	threads = []
	for i in range(numthread):
		thread = threading.Thread(target = fun, args = ())
		thread.setName('Thread-{0:2}'.format(i+1))
		thread.start()
		threads.append(thread)

	while True:
		key = input('press \'q\' to exit\n') 
		if key == 'q': 
			break
		else:
			pass

	exitflag.set()
	for thread in threads:	thread.join()
	logger.debug('Main thread Exit.')










