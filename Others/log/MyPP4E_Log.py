#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-25 15:13:53
# @Author  : 王国安 
# @email   : 18909311025@189.cn 
# @Version : 1.0
"""
  摘自：python标准模块--logging http://www.cnblogs.com/zhbzz2007/p/5943685.html
  1、测试使用logging模块，使用logging.Logger类
  2、loglevel
    NOTSET = 0
    DEBUG = 10
    INFO = 20
    WARN = WARNING = 30
    ERROR = 40
    CRITICAL = FATAL = 50
"""
import logging

def mypp4e_log():
	logger = logging.Logger(name = 'MyPP4Elog')
	logger.setLevel(logging.DEBUG)


	#创建Filehandler,设置log级别为INFO,设置log格式其风格为'{'
	handler = logging.FileHandler('e:\ProgrammingPython\MyPP4E\Mypp4eLog.txt')      
	handler.setLevel(logging.INFO)                
	formatter1 = logging.Formatter('{asctime}|{name}|{pathname}|{levelno}|{levelname}|{message}',style = '{')	          
	handler.setFormatter(formatter1)

	#log同时也输出到stderr，设置log级别为DEBUG,设置log格式其风格为'{'
	console = logging.StreamHandler()
	console.setLevel(logging.DEBUG)
	formatter2 = logging.Formatter('{asctime}|{name}|{levelno}|{levelname}|{message}',style = '{')
	console.setFormatter(formatter2)	

	#将filehandler和console都添加到当前logger对象
	logger.addHandler(handler)
	logger.addHandler(console)
	return logger

if __name__ == '__main__':
	logger = mypp4e_log()
	logger.debug('Houston, we have a %s', 'thorny problem')
	logger.info('Houston, we have a %s', 'interesting problem')
	logger.error('Houston, we have a %s', 'major problem')
	logger.warning('Houston, we have a %s', 'bit of a problem')
	logger.critical('Houston, we have a %s', 'major disaster')






