#coding=utf-8
'''
Created on 2017年6月6日

@author: 王国安
'''
from initdata import tom
import shelve
db = shelve.open('people-shelve')
sue = db['sue']                     #fetch sue
sue['pay'] *=1.50
db['sue'] = sue                     #update sue
db['tom'] = tom                     #append a new record
db.close() 