#coding=utf-8
'''
Created on 2017年6月6日

@author: 王国安
'''
import pickle

suefile = open('sue.pkl','rb')
sue = pickle.load(suefile)
suefile.close()

sue['pay'] *=1.10

suefile = open('sue.pkl','wb')
pickle.dump(sue,suefile)
suefile.close()


