#coding=utf-8
'''
Created on 2017年6月19日

@author: 王国安
'''
import os
print('setenv...', end=' ')
print(os.environ['USER'])

os.environ['USER'] = 'Brian'
os.system('python echoenv.py')

os.environ['USER'] = 'Arthur'
os.system('python echoenv.py')

os.environ['USER'] = input('?')
print(os.popen('python echoenv.py').read())
