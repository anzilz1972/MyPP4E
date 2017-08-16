#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-16 11:38:14
# @Author  : 王国安 
# @email   : 18909311025@189.cn 
# @Version : $Id$

import os,sys
from multiprocessing import Process,Value,Array

procs = 3
count = 0 

def showdata(label,val,arr):
	#打印数据
	msg = '{}: pid:{}, global:{}, value:{}, array:{}'
	#logger.info(msg.format(label,os.getpid(),count,val.value,list(arr)))
	print(msg.format(label,os.getpid(),count,val.value,list(arr)))

def update(val,arr):
	global count
	count += 1
	val.value += 1
	for i in range(3): arr[i] += 1

if __name__ == '__main__':
	scalar = Value('i',0)                         #共享内存是进程/线程安全的
	vector = Array('d',procs)                     

	#在父进程中显示起始值
	showdata('parent',scalar,vector)

	#派生子进程，传入共享内存
	p = Process(target = showdata, args = (' child',scalar,vector))
	p.start()
	p.join()

	#传入父进程中更新过的共享内存，等待每次传入结束
	#每个子进程看到了父进程中到现在为止对args的更新
	print('\nloop1 (updates in parent,serial children)...')
	for i in range(procs):
		count += 1
		scalar.value += 1
		vector[i] += 1
		p = Process(target = showdata, args = ('process {}'.format(i),scalar,vector))
		p.start()
		p.join()

	#同上，不过允许所有子进程并行运行
	#所有进程都看到了最近一次迭代的结果
	print('\nloop2 (updates in parent,parallel children)...')
	ps = []
	for i in range(procs):
		count += 1
		scalar.value += 1
		vector[i] += 1
		p = Process(target = showdata, args = ('process {}'.format(i),scalar,vector))
		p.start()
		ps.append(p)
	for p in ps:p.join()

	#共享内存在派生子进程中更新，子进程串行运行，等待每个更新结束
	print('\nloop3 (updates in serial children)...')
	for i in range(procs):
		p = Process(target = update, args = (scalar,vector,))
		p.start()
		p.join()
	showdata('parent temp',scalar,vector)

	#同上，但是允许子进程并行更新
	print('\nloop4 (updates in parallel children)...')
	ps = []
	for i in range(procs):
		p = Process(target = update, args = (scalar,vector,))
		p.start()
		ps.append(p)
	for p in ps: p.join()
	showdata('parent end',scalar,vector)












