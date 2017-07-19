#coding=utf-8
'''
Created on 2017年6月6日

@author: 王国安
'''
import shelve
db = shelve.open('people-shelve')
for key in db:
    print(key,'=>\n  ',db[key])
print(db['sue']['name'])
db.close()