#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-27 15:41:06
# @Author  : 王国安 
# @email   : 18909311025@189.cn 
# @Version : 1.0

"""
  1、摘自python-3.5.3-docs-html/library/multiprocessing.html的代码片段
  2、演示：
      1、use pipe,Exchanging objects between processes
      2、The Pipe() function returns a pair of connection objects 
         connected by a pipe which by default is duplex (two-way).
      3、模拟《血染雪山堡》，两个子进程实现双向会话，父进程使用Event()事件通知子进程结束
  3、结论：
  	 Multiprocessing.Pipe()创建的是全双工duplex (two-way)的管道，连接到管道两端的进程在任意
  	 时刻都可以进行读写操作，而不用担心管道阻塞
"""

import sys,random,time,multiprocessing
from multiprocessing import Process,Pipe,Event,Value,Array

sys.path.append('..\..\..\others\log')					#将log模块加入到系统目录中
from MyPP4E_Log import Mypp4elog
logger = Mypp4elog()									#get logger object


def readtoEOF(conn,myName):
	while True:
		if conn.poll() == True:
			words = conn.recv()
			logger.info('{} recived: {}'.format(myName,words))
		else:
			break


def call(myname,yourname,conn,exitEvent):
	pID = multiprocessing.current_process().pid
	logger.info('{} is running,PID: {}'.format(myname,pID))
	i = 1
	while True:
		###第一步：检查管道中是否有可读的数据；如果有，读出并打印
		while True:
			if conn.poll() == True:
				words = conn.recv()
				logger.info('{} recived: {}'.format(myname,words))
			else:
				break
		###第二步：休眠随机时间
		time.sleep(random.randint(0,3))
		###第三步：探测父进程是否要求子进程退出，如果标志已经设置则退出
		if exitEvent.is_set() == True:
			logger.info('{} has detected exit_flag and will exit'.format(myname))
			break
		###第四步：向管道中写数据
		conn.send('{} call {}, {}'.format(myname,yourname,i))
		i += 1


if __name__ == '__main__':

	exitFlag = Event()                                 #子进程退出标志，由父进程根据条件设置
	exitFlag.clear()                                   #初始化不设置

	logger.info('Parent Process running...')

	broadsword,dannyboy = Pipe()
	p1 = Process(target = call, args = ('BroadSword','Danny  Boy',broadsword,exitFlag,))
	p2 = Process(target = call, args = ('Danny  Boy','BroadSword',dannyboy,exitFlag,))
	p1.start()
	p2.start()

	############################# Caution ########################################
	#1、两个子进程启动后，在主进程中不能马上调用input()函数，否则会导致子进程阻塞
	#2、切切：在子进程都启动后，建议主进程休眠一段时间，之后再调用input()函数
	#3、调试这个bug花了我整整一天时间
	time.sleep(5)
	input('press any key to exit...\n')
	############################# Caution ########################################

	exitFlag.set()
	p1.join()
	p2.join()

	#两个子进程已经结束，但管道中可能有未读完的数据，处理后关闭管道
	readtoEOF(broadsword,'BroadSword')
	readtoEOF(dannyboy,'Danny  Boy')
	broadsword.close()
	dannyboy.close()

	logger.info('Parent Process Exit.')


