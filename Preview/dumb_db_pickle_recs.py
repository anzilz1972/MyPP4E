#coding=utf-8
'''
Created on 2017年6月6日

@author: 王国安
'''
import pickle,glob

for filename in glob.glob('*.pkl'):    #针对bob,sue,tom
    recfile = open(filename,'rb')
    record = pickle.load(recfile)
    recfile.close()
    print(filename, '=>\n  ',record)

suefile = open('sue.pkl','rb')
print(pickle.load(suefile)['name'])
suefile.close()