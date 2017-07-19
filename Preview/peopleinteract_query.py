#coding=utf-8
'''
Created on 2017年6月7日

@author: 王国安
'''
#interactive queries
import shelve
fieldnames = ('name', 'age', 'job', 'pay')
maxfield = max(len(f) for f in fieldnames)
db = shelve.open('class-shelve')

while True:
    key = input('\nkey? =>')   #' '键或者空行，空行退出
    if not key: break
    try:
        record = db[key]
    except:
        print('No such key "{}"!'.format(key))
    else:
        for field in fieldnames:
            print(field.ljust(maxfield), '=>', getattr(record,field))

print('bye bye!')

