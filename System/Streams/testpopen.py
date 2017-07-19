#coding=utf-8
'''
Created on 2017年6月22日

@author: 王国安
'''

#import subprocess,sys,os
from subprocess import Popen,PIPE,STDOUT
import os

def writetofile():
    outputf = open('hello-out.txt','a')
    proc = Popen('python hello-out.py',universal_newlines=True,stdout = outputf)
    proc.wait()
    outputf.close()

def writetopipe():
    proc = Popen('python hello-out.py',universal_newlines=True,stdout = PIPE,stderr=STDOUT)
    print(proc.stdout.read())
    proc.wait()


 
