#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-28 09:54:32
# @Author  : 王国安 
# @email   : 18909311025@189.cn 
# @Version : $Id$

"""
  1、参考：《python进程池：multiprocessing.pool》
            http://www.cnblogs.com/kaituorensheng/p/4465768.html 
  2、演示：
     1）使用进程池
     2）使用阻塞的进程池
     3）使用进程池并获取结果
     4）使用logger输出信息：由于logging.logger是线程和进程安全的，因此能保证进程第一时间输出到stdout上，避免使用print函数带来的输出不同步问题
  3、阻塞式进程池和非阻塞式进程池实验结果：参见本程序尾部
"""

import multiprocessing,time,sys

sys.path.append('..\..\..\others\log')					#将log模块加入到系统目录中
from MyPP4E_Log import Mypp4elog
logger = Mypp4elog()									#get logger object



def f(msgId):
	pID = multiprocessing.current_process().pid
	logger.info('hello, {}. process id:{}'.format(msgId,pID))
	time.sleep(3)
	logger.info('byebye {}. process id:{}'.format(msgId,pID))
	return pID

#非阻塞进程池
def pool_unblocked(r):
	for i in range(numprocess):
		r.append(pool.apply_async(f,(i,)))

#阻塞式进程池
def pool_blocked(r):
	for i in range(numprocess):
		r.append(pool.apply(f,(i,)))


if __name__ == '__main__':
	numprocess = 120                                                 #总共要运行的进程数量
	pool_capacity = multiprocessing.cpu_count()                     #本机cpu数量(核) ，用来设定进程池容量pool_capacity
	pool = multiprocessing.Pool(processes = pool_capacity)

	result = []
	pool_unblocked(result)  #调用非阻塞的进程池
	#pool_blocked(result)     #调用阻塞式进程池

	logger.info('main process,id:{}'.format(multiprocessing.current_process().pid))
	pool.close()
	pool.join()
    
    #获取进程执行结果并打印
    #***阻塞模式不返回结果，因此会引发异常
	for res in result:
		try:
			logger.info(':::{}'.format(res.get()))                       
		except AttributeError:
			logger.warning('res.get() error:AttributeError.')
	logger.info('Sub-processes done.')

############################################################################################################################################
"""
在非阻塞状态下工作时，
    1）系统一次性将pool_capacity（本机CPU数量）个进程放入进程池内，这些进程在每个*单独*的CPU上并行运行
    2）一个CPU上的进程运行完毕后，下一个排队的进程在此CPU上开始运行
    3）注意：在此过程中，在一个CPU上的进程PID是恒定不变的
详细结果如下：
main process,id:12860|2017-07-28 11:31:34,303|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
hello, 0. process id:3240|2017-07-28 11:31:34,383|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
hello, 1. process id:13256|2017-07-28 11:31:34,385|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
hello, 2. process id:1932|2017-07-28 11:31:34,388|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
hello, 3. process id:256|2017-07-28 11:31:34,393|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
byebye 0. process id:3240|2017-07-28 11:31:37,383|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
hello, 4. process id:3240|2017-07-28 11:31:37,383|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
byebye 1. process id:13256|2017-07-28 11:31:37,385|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
hello, 5. process id:13256|2017-07-28 11:31:37,385|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
byebye 2. process id:1932|2017-07-28 11:31:37,388|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
hello, 6. process id:1932|2017-07-28 11:31:37,388|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
byebye 3. process id:256|2017-07-28 11:31:37,393|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
hello, 7. process id:256|2017-07-28 11:31:37,393|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
byebye 4. process id:3240|2017-07-28 11:31:40,384|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
hello, 8. process id:3240|2017-07-28 11:31:40,384|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
byebye 5. process id:13256|2017-07-28 11:31:40,386|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
hello, 9. process id:13256|2017-07-28 11:31:40,386|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
byebye 6. process id:1932|2017-07-28 11:31:40,389|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
hello, 10. process id:1932|2017-07-28 11:31:40,389|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
byebye 7. process id:256|2017-07-28 11:31:40,394|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
hello, 11. process id:256|2017-07-28 11:31:40,394|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
byebye 8. process id:3240|2017-07-28 11:31:43,384|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
byebye 9. process id:13256|2017-07-28 11:31:43,386|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
byebye 10. process id:1932|2017-07-28 11:31:43,389|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
byebye 11. process id:256|2017-07-28 11:31:43,395|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
Sub-processes done.|2017-07-28 11:31:43,466|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
[Finished in 9.4s]
"""
############################################################################################################################################
"""
在阻塞状态下工作时，
    1）系统一次只将一个进程在一个CPU上运行，其他进程等待；待此进程运行完毕后，系统将下一个进程在另一个CPU上运行；
    2）总体看，阻塞状态下的进程池是以*串行*方式运行各个进程，系统运行效率只有非阻塞状态下的（1/pool_capacity）
详细结果如下：
hello, 0. process id:10736|2017-07-28 11:29:17,711|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
byebye 0. process id:10736|2017-07-28 11:29:20,711|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
hello, 1. process id:11376|2017-07-28 11:29:20,712|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
byebye 1. process id:11376|2017-07-28 11:29:23,713|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
hello, 2. process id:11248|2017-07-28 11:29:23,714|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
byebye 2. process id:11248|2017-07-28 11:29:26,715|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
hello, 3. process id:13068|2017-07-28 11:29:26,716|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
byebye 3. process id:13068|2017-07-28 11:29:29,716|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
hello, 4. process id:10736|2017-07-28 11:29:29,717|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
byebye 4. process id:10736|2017-07-28 11:29:32,718|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
hello, 5. process id:11376|2017-07-28 11:29:32,719|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
byebye 5. process id:11376|2017-07-28 11:29:35,719|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
hello, 6. process id:11248|2017-07-28 11:29:35,720|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
byebye 6. process id:11248|2017-07-28 11:29:38,720|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
hello, 7. process id:13068|2017-07-28 11:29:38,721|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
byebye 7. process id:13068|2017-07-28 11:29:41,722|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
hello, 8. process id:10736|2017-07-28 11:29:41,722|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
byebye 8. process id:10736|2017-07-28 11:29:44,724|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
hello, 9. process id:11376|2017-07-28 11:29:44,725|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
byebye 9. process id:11376|2017-07-28 11:29:47,726|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
hello, 10. process id:11248|2017-07-28 11:29:47,727|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
byebye 10. process id:11248|2017-07-28 11:29:50,727|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
hello, 11. process id:13068|2017-07-28 11:29:50,728|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
byebye 11. process id:13068|2017-07-28 11:29:53,730|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
main process,id:1400|2017-07-28 11:29:53,730|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
Sub-processes done.|2017-07-28 11:29:53,837|E:\ProgrammingPython\MyPP4E\System\Processes\python3.5.3samples\process_Pool1.py|20|INFO
[Finished in 36.4s]
"""