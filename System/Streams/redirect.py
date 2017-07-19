#coding=utf-8
'''
Created on 2017年6月21日

@author: 王国安
file-like objects that save standard output text in a string and provide
standard input text from a string; redirect runs a pass-in function
with its output and input streams reset to these file-like class objects; 
'''
import sys
class Output:                              #Output类模拟输出文件
    def __init__(self):                
        self.text = ''                     #将输出结果存储在'text'字符串中  
    def write(self,string):
        self.text += string
    def writelines(self,lines):
        for line in lines:self.write(line)
        
class Input:                               #Input类模拟 输入文件
    def __init__(self,inStr=''):           #初始化对象时，将输入内容缓存在'text'字符串中
        self.text = inStr                   
    def read(self,size=None):              #读取size指定的字符数或者所有数据  
        if size==None:
            res,self.text = self.text,''
        else:
            res,self.text = self.text[:size],self.text[size:]
        return res
    def readline(self):                   #读取并返回一行数据 
        eoln = self.text.find('\n')       #'eoln'-->end of line
        if eoln == -1:
            res,self.text = self.text,''
        else:
            res,self.text = self.text[:eoln+1],self.text[eoln+1:]
        return res

def redirect(function,pargs,kargs,input):          #为被调用函数重定向I/O
    savestreams = sys.stdin,sys.stdout             #将原I/O对象缓存
    sys.stdin,sys.stdout = Input(input),Output()   #重定向sys.stdin,sys.stdout至文件类对象
    try:
        result = function(*pargs,**kargs)
        output = sys.stdout.text
    finally:
        sys.stdin,sys.stdout = savestreams         #恢复缓存的I/O对象
    return (result,output)
    
    
         
    
