#coding=utf-8
'''
Created on 2017年6月7日

@author: 王国安
'''
import shelve
from person import Person

fieldnames = ('name', 'age', 'job', 'pay')
db = shelve.open('class-shelve')

while True:
    key = input('\nkey? =>')
    if not key: break
    if key in db:
        record = db[key]                       #更新已存在的记录  
    else:                                      #或者创建/保存新纪录
        record = Person(name='?' ,age='?')     #eval: 引号字符串
    for field in fieldnames:
        currval = getattr(record,field)
        newtext = input('\t[{}]={}\n\t\tnew?=>'.format(field,currval))
        if newtext:
            setattr(record,field,eval(newtext))
    db[key] = record

db.close()
    