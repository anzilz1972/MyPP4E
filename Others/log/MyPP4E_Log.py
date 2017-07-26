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

"""
内部函数定义，只供mypp4e_log()函数和class Mypp4elog使用
"""
#创建filehandler,以便将Log写入文件
def _CreatFileHandler(rotateLog = False, fileLogLevel =logging.WARNING):
	fileFormatter = logging.Formatter('{message}|{asctime}|{pathname}|{levelno}|{levelname}',style = '{')
	if rotateLog:
		#创建RotatingFileHandler,可以实现日志回滚;每个log文件大小为1M,上限100个文件
		handler = RotatingFileHandler('rlog.txt', maxBytes = 1024*1024, backupCount = 100)
	else:
		#创建Filehandler
		handler = logging.FileHandler('log.txt')      
	handler.setFormatter(fileFormatter)
	handler.setLevel(fileLogLevel)
	return handler

#log输出到stderr
def _CreatStderrHandler(stderrLogLevel = logging.DEBUG):
	stderrformatter = logging.Formatter('{message}|{asctime}|{pathname}|{levelno}|{levelname}',style = '{')
	handler = logging.StreamHandler()
	handler.setFormatter(stderrformatter)	
	handler.setLevel(stderrLogLevel)
	return handler


########################################################外部可调用函数和类###############################################
"""
   mypp4e_log():
   1、class Mypp4elog()类的简化实现，更多参数采用默认值
   2、调用此函数，返回一个logger对象；此logger对象默认产生file log，并输出stderr log
"""
def mypp4e_log(rotateLog = False, stderrLog = True):
	logger = logging.Logger(name = 'MyPP4Elog')
	logger.addHandler(_CreatFileHandler(rotateLog))
	if stderrLog:
		logger.addHandler(_CreatStderrHandler())
	return logger


"""
   class Mypp4elog:提供更多的可选参数对logger进行初始化
"""
class Mypp4elog(logging.Logger):
	"""
	__init__() Params:
	
	name:			logger默认名称为"MyPP4Elog"
	rotateLog:		确定文件日志是common file Log还是rotate fiel Log，默认为普通文件日志
	fileLogLevel:	默认为WARNING级别，包括rotateLog									
	stderrLog:		默认需要stderr log，向stderr输出
	stderrLogLevel：默认为DEBUG级别
	"""
	def __init__(self, name = 'MyPP4Elog', rotateLog = False, fileLogLevel =logging.WARNING, stderrLog = True, stderrLogLevel = logging.DEBUG):
		
		logging.Logger.__init__(self,name)

		#将文件handler添加到此logger
		self.addHandler(_CreatFileHandler(rotateLog,fileLogLevel))						
		

		#如果需要stderrLog,将StderrHandler添加到此logger 
		if stderrLog:
			self.addHandler(_CreatStderrHandler(stderrLogLevel))	                



if __name__ == '__main__':
	"""
	logger = mypp4e_log()
	logger.debug('Houston, we have a %s', 'thorny problem')
	logger.info('Houston, we have a %s', 'interesting problem')
	logger.warning('Houston, we have a %s', 'bit of a problem')
	logger.error('Houston, we have a %s', 'major problem')
	logger.critical('Houston, we have a %s', 'major disaster')

	"""
	logger = Mypp4elog()
	logger.debug('Houston, we have a %s', 'thorny problem')
	logger.info('Houston, we have a %s', 'interesting problem')
	logger.warning('Houston, we have a %s', 'bit of a problem')
	logger.error('Houston, we have a %s', 'major problem')
	logger.critical('Houston, we have a %s', 'major disaster')
	print(logger.name)







