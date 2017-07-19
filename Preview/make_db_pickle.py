#coding=utf-8
'''
Created on 2017年6月6日

@author: 王国安
'''
from initdata import db
import pickle
dbfile = open('people-pickle', 'wb') #使用3.X的二进制模式文件
pickle.dump(db,dbfile)
dbfile.close()