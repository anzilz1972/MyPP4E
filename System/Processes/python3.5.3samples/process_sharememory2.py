#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-27 17:15:41
# @Author  : 王国安 
# @email   : 18909311025@189.cn 
# @Version : 1.0

"""
  1、摘自python-3.5.3-docs-html/library/multiprocessing.html的代码片段
  2、演示：
      Sharing state between processes,method one:use shared memory
      1)As mentioned above, when doing concurrent programming it is usually best to avoid using shared state as far as possible. This is particularly true when using multiple processes.
	  However, if you really do need to use some shared data then multiprocessing provides a couple of ways of doing so.
	  2)Data can be stored in a shared memory map using Value or Array.
"""

from multiprocessing import Process,Value
import time

def f(n) :
	while True:
		if n.value == True:
			print('get exit signal!')
			break
		time.sleep(2)
	print('Child Process exit.')

if __name__ == '__main__':
	num = Value('b', False)

	p = Process(target = f, args = (num,))
	p.start()

	input('press any key to exit...')
	num.value = True
	p.join()
	print('Parent Process exit.')




