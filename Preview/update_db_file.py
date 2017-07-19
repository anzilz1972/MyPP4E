#coding=utf-8
'''
Created on 2017年6月6日

@author: 王国安
'''
from make_db_file import loadDbase,storeDbase
db = loadDbase()
db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'
for key in db:
    print(key,'=>\n  ',db[key])
storeDbase(db)
