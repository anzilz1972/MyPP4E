#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-02 08:25:24
# @Author  : 王国安 
# @email   : 18909311025@189.cn 
# @Version : 1.0

import sys,signal,time

def now():
	return time.ctime(time.time())                            #当前时间的字符串

def onSignal(signum,stackframe):                              #python信号处理器
    print('Got signal',signum,'at',now())

signum = int(sys.argv[1])
signal.signal(signum,onSignal)
while True:time.sleep(1)



