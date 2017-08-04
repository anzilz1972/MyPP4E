#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-04 11:39:48
# @Author  : 王国安 
# @email   : 18909311025@189.cn 
# @Version : 1.0

import os
from multiprocessing import Process,Lock

def whoami(label,lock):
	msg = '{}: name:{}, pid:{}'
	with lock:
		print(msg.format(label,__name__,os.getpid()))

if __name__ == '__main__':
	lock =Lock()
	whoami('function call',lock)

	p = Process(target=whoami ,args=('spawned child',lock))
	p.start()
	p.join()

	for i in range(5):
		Process(target=whoami ,args=('run process {}'.format(i),lock)).start()

	with lock:
		print('Main process exit.')
