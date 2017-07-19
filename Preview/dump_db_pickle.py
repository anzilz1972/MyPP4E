#coding=utf-8
'''
Created on 2017年6月6日

@author: 王国安
'''
import pickle
dbfile = open('people-pickle','rb')   #使用3.X的二进制模式文件
db = pickle.load(dbfile)
dbfile.close()

for key in db:
    print(key, '=>\n  ',db[key])
