#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-25 15:13:53
# @Author  : 王国安 
# @email   : 18909311025@189.cn 
# @Version : 1.0
"""
  1、摘自：python标准模块--logging http://www.cnblogs.com/zhbzz2007/p/5943685.html
  2、测试使用logging模块，使用logging.Logger类
  3、loglevel
    NOTSET = 0
    DEBUG = 10
    INFO = 20
    WARN = WARNING = 30
    ERROR = 40
    CRITICAL = FATAL = 50
"""
import logging,time
from logging.handlers import RotatingFileHandler


def mypp4e_log(rotateLog = True, stderrLog = True):
	logger = logging.Logger(name = 'MyPP4Elog')
	logger.setLevel(logging.DEBUG)

	fileFormatter = logging.Formatter('{message}|{asctime}|{pathname}|{levelno}|{levelname}',style = '{')
	if rotateLog:
		#使用RotatingFileHandler,可以实现日志回滚
		#创建RotatingFileHandler,设置log级别为WARNING，设置log格式其风格为'{'
		#每个log文件大小为1M,上限100个文件
		rHandler = RotatingFileHandler('rlog.txt', maxBytes = 1024*1024, backupCount = 100)
		rHandler.setLevel(logging.WARNING)
		rHandler.setFormatter(fileFormatter)
		logger.addHandler(rHandler)					#正常log文件log.txt
	else:
		#创建Filehandler,设置log级别为WARNING,设置log格式其风格为'{'
		handler = logging.FileHandler('log.txt')      
		handler.setLevel(logging.WARNING)                
		handler.setFormatter(fileFormatter)
		logger.addHandler(handler)	                #可回滚log文件rlog.txt

	#log也可以输出到stderr，设置log级别为DEBUG,设置log格式其风格为'{'
	if stderrLog:
		console = logging.StreamHandler()
		console.setLevel(logging.DEBUG)
		consoleformatter = logging.Formatter('{message}|{asctime}|{pathname}|{levelno}|{levelname}',style = '{')
		console.setFormatter(consoleformatter)	
		logger.addHandler(console)
	return logger

class Mypp4e_log(logging.Logger):

	def __init__(self,):









if __name__ == '__main__':
	logger = mypp4e_log()
	for i in range(100000):
		logger.debug('Houston, we have a %s', 'thorny problem')
		logger.info('Houston, we have a %s', 'interesting problem')
		logger.warning('Houston, we have a %s', 'bit of a problem')
		logger.error('Houston, we have a %s', 'major problem')
		logger.critical('Houston, we have a %s', 'major disaster')
		time.sleep(2)






