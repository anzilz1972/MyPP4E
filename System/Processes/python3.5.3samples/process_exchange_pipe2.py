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
      3、模拟《血染雪山堡》，两个子进程实现双向会话，父进程通知会话结束
"""

import sys,random,time
import multiprocessing as mp
from multiprocessing import Process,Pipe,Event,Value

sys.path.append('..\..\..\others\log')					#将log模块加入到系统目录中
from MyPP4E_Log import Mypp4elog
logger = Mypp4elog()									#get logger object



def call(myname,yourname,conn,exitEvent):
	logger.info('{} is running,PID: {}'.format(myname,mp.current_process().pid))

	i = 1
	while True:
		while True:
			if conn.poll() == True:
				words = conn.recv()
				logger.info('{} recived: {}'.format(myname,words))
			else:
				break

		time.sleep(random.randint(0,3))

		"""*************multiprocessing模块下的Event实现有bug，调用is_set()都会阻塞进程	
		if exitEvent.is_set() == True:
			logger.debug('{} detected exit flag is set,circle:{}'.format(myname,i))
			break
		else:
			logger.debug('{} detected exit flag is *NOT* set,circle:{}'.format(myname,i))
		"""

		###只好用multiprocessing模块的共享内存，实现进程间通信	
		#if exitEvent.value == True:break

		conn.send('{} called {}, {}'.format(myname,yourname,i))
		i += 1


	logger.info('{} will exit,PID: {}'.format(myname,mp.current_process().pid))

if __name__ == '__main__':
	logger.info('Parent Process running...')
	exitFlag = Value('b',False)

	broadsword,dannyboy = Pipe()
	p1 = Process(target = call, args = ('BroadSword','Danny  Boy',broadsword,exitFlag))
	p2 = Process(target = call, args = ('Danny  Boy','BroadSword',dannyboy,exitFlag))
	p1.start()
	p2.start()

	input('press any key to exit...\n')

	exitFlag.value = True
	p1.join()
	p2.join()
	broadsword.close()
	dannyboy.close()
	logger.info('Parent Process Exit.')


