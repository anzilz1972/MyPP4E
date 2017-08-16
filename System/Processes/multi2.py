#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-16 10:52:22
# @Author  : 王国安 
# @email   : 18909311025@189.cn 
# @Version : $Id$

import os,sys
from multiprocessing import Process,Pipe

sys.path.append('..\..\others\log')					#将log模块加入到系统目录中
from MyPP4E_Log import Mypp4elog
logger = Mypp4elog()									#get logger object

def sender(pipe):
	#在匿名管道上向父进程发送对象
	pipe.send(['spam'] + [42,'eggs'])
	pipe.close()

def talker(pipe):
	#通过管道发送和接收对象
	pipe.send(dict(name = 'bob', spam =42))
	reply = pipe.recv()
	print('talker got:',reply)

if __name__ == '__main__':
	parentEnd,childEnd = Pipe()
	Process(target = sender, args = (childEnd,)).start()
	print('parent got:',parentEnd.recv())
	parentEnd.close()

	parentEnd,childEnd = Pipe()
	child = Process(target = talker,args = (childEnd,))
	child.start()
	print('parent got:',parentEnd.recv())
	parentEnd.send({x * 2 for x in 'spam'})
	child.join()
	print('parent exit')
