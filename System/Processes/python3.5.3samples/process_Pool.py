#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-28 08:21:49
# @Author  : 王国安 
# @email   : 18909311025@189.cn 
# @Version : $Id$

"""
  1、摘自python-3.5.3-docs-html/library/multiprocessing.html的代码片段
  2、演示：
      The Pool class represents a pool of worker processes. It has methods which allows tasks to be offloaded to the worker processes in a few different ways.
"""

from multiprocessing import Pool,TimeoutError
import time
import os

def f(x):
	return x*x

if __name__ == '__main__':
	#start 4 worker processes
	with Pool(processes = 4) as pool:

		#print([0, 1, 4, 9, 16, 25, 36, 49, 64, 81])
		print(pool.map(f,range(10)))

		#print same numbers in arbitrary order
		for i in pool.imap_unordered(f,range(10)):
			print(i)

		#evaluate 'f(20)' asynchronously
		res = pool.apply_async(f,(20,))                    #runs in *only* one process
		print('f(20) =>',res.get(timeout = 1))             #prints '400'

		#evaluete 'os.getpid()' asynchronously
		res = pool.apply_async(os.getpid,())               #runs in *only* one process
		print('Pid:', res.get(timeout = 1))                #print the pid of that process


		#make a single worker sleep for 10 secs
		res = pool.apply_async(time.sleep,(10,))
		try:
			print(res.get(timeout = 1))
		except TimeoutError:
			print('We lacked patience and got a multiprocessing.Timeouterror.')

		print('For the moment, the pool remains available for more work')

 	# exiting the 'with'-block has stopped the pool
	print('now the pool is closed and no longer available.')



