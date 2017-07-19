#coding=utf-8
'''
Created on 2017年6月7日

@author: 王国安
'''
import shelve
db = shelve.open('class-shelve')

for key in db:
    print(key, '=>\n\t',db[key].name, db[key].pay)
    print('\t',db[key])

db.close()
