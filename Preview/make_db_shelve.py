#coding=utf-8
'''
Created on 2017年6月6日

@author: 王国安
'''

from initdata import bob,sue
import shelve

db = shelve.open('people-shelve')
db['bob'] = bob
db['sue'] = sue
db.close()