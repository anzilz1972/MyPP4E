#coding=utf-8
'''
Created on 2017年6月6日

@author: 王国安
'''
from initdata import bob,sue,tom
import pickle

for (key,record) in [('bob',bob),('tom',tom),('sue',sue)]:
    recfile = open(key + '.pkl', 'wb')
    pickle.dump(record,recfile)
    recfile.close()