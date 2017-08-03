#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-27 15:41:06
# @Author  : 王国安 
# @email   : 18909311025@189.cn 
# @Version : 1.0

"""
  1、摘自python-3.5.3-docs-html/library/multiprocessing.html的代码片段
  2、演示：
      1、use pipe,Exchanging objects between processes
      2、The Pipe() function returns a pair of connection objects 
         connected by a pipe which by default is duplex (two-way).
      3、实现双向会话
"""

"""
《二》看电影

Tom：Hello. May I speak to Mary, please?
Mary：Speaking. Who’s calling, please?
Tom：Hi, Mary. This is Tom.
Mary：Oh, hi, Tom. How’ve you been?
Tom：Just fine. I say. Aren’t you busy tomorrow evening?
Mary：Let me see. Uh-huh…no, I guess I’ll be free.
Tom：Well, uh…why not dine out together and go to the movies?
Mary：Sounds like a good idea.
Tom：Okay. I’ll pick you up at 6:00.
Mary：Thank you for inviting me. See you then. Bye, Tom.
Tom：Bye now.
"""




from multiprocessing import Process,Pipe
import sys

sys.path.append('..\..\..\others\log')					#将log模块加入到系统目录中
from MyPP4E_Log import Mypp4elog
logger = Mypp4elog()									#get logger object


#Tom is speaking
tSentences = [
'Hello. May I speak to Mary, please?',
'Hi, Mary. This is Tom.',
'Just fine. I say. Aren’t you busy tomorrow evening?',
'Well, uh…why not dine out together and go to the movies?',
'Okay. I’ll pick you up at 6:00.',
'Bye now.'
]

#Mary is speaking
mSentences = [
'Speaking. Who’s calling, please?',
'Oh, hi, Tom. How’ve you been?',
'Let me see. Uh-huh…no, I guess I’ll be free.',
'Sounds like a good idea.',
'Thank you for inviting me. See you then. Bye, Tom.'
]



def speak(mary,Sentences):
	idx = 0
	while True:
		words = mary.recv()
		logger.info('Tom: {}'.format(words))
		if idx < len(Sentences):
			mary.send(Sentences[idx])
		if 'Bye' in words or 'bye' in words:break
		idx +=1
	mary.close()

if __name__ == '__main__':
	Tom,Mary = Pipe()
	p = Process(target = speak, args = (Mary,mSentences))
	p.start()

	idx = 0
	while True:
		Tom.send(tSentences[idx])
		idx +=1
		words = Tom.recv()
		logger.info('Mary: {}'.format(words))
		if 'Bye' in words or 'bye' in words:break

	if idx == len(tSentences)-1: Tom.send(tSentences[idx])                    #补发最后一句话

	p.join()
	Tom.close()
	

