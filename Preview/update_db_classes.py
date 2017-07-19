#coding=utf-8
'''
Created on 2017年6月7日

@author: 王国安
'''
import shelve
db = shelve.open('class-shelve')

sue = db['sue']
sue.giveRaise(0.25)
db['sue'] = sue

tom = db['tom']
tom.giveRaise(0.20)
db['tom'] = tom

db.close()
