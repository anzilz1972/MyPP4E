#coding=utf-8
'''
Created on 2017年6月6日

@author: 王国安
'''
from make_db_file import loadDbase
db = loadDbase()
for key in db:
    print(key,'=>\n  ',db[key])
