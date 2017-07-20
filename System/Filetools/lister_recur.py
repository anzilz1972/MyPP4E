#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-20
# @Author  : 王国安 
# @email   : 18909311025@189.cn 
# @Version : 1.0
# @feature ：
#		以递归方式遍历目录树中的文件,遍历是排除excludedirs指定的相关目录
#
#

import os,sys
def mylister(currdir,*excldirs):

	#将无需遍历的目录转为小写字符串，存储于excludedirs
	excludedirs = [aItem.lower() for aItem in excldirs]

	print('\n[' + currdir + ']')
	#遍历当前目录，file==》当前目录下的子目录或文件
	for file in os.listdir(currdir):
		path = os.path.join(currdir,file)

		if not os.path.isdir(path):
			#file是一个文件，打印
			print(' ' + path)
		else:
			#file是一个子目录，判断该子目录是否需要遍历；
			#如果不需要则跳过
			if file.lower() not in  excludedirs: mylister(path,*excldirs)



if __name__ == '__main__':
	#收集命令行参数指定的，无需遍历的目录，存储在exdirs中
	exdirs = []
	for i in range(2,len(sys.argv)):
		exdirs.append(sys.argv[i])

	#argv[1]==>待遍历目录
	#exdirs ==>无需遍历的子目录
	mylister(sys.argv[1],*exdirs)




