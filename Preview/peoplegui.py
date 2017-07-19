#coding=utf-8
'''
Created on 2017年6月7日

@author: 王国安
实现一个图形界面，用于查看和更新存储于shelve中的类实例；
该shelve保存在脚本运行的机器上，可能是一个或多个本地文件
'''

from tkinter import *
from tkinter.messagebox import showerror,showinfo
import shelve

shelvename = 'class-shelve'
fieldnames = ('name', 'age', 'job', 'pay')

def makeWidgets():
    global entries
    window = Tk()
    window.title('People Shelve')
    form = Frame(window)
    form.pack()
    entries = {}
    for(idx,label) in enumerate(('key',) + fieldnames): 
        lab = Label(form, text=label)
        ent = Entry(form)
        lab.grid(row=idx, column=0)
        ent.grid(row=idx, column=1)
        entries[label] = ent
    Button(window, text='Fetch', command=fetchRecord).pack(side=LEFT)
    Button(window, text='Update', command=updateRecord).pack(side=LEFT)
    Button(window, text='Quit', command=window.quit).pack(side=RIGHT)
    return window

def fetchRecord():
    key = entries['key'].get()
    try:
        record = db[key]
    except:
        showerror(title='Error', message='No such key! ==> {} '.format(key))
    else:
        for field in fieldnames:
            entries[field].delete(0,END)
            entries[field].insert(0,repr(getattr(record,field)))
    

def updateRecord():
    key = entries['key'].get()
    newrecord = False
    if key in db:
        record = db[key]                        #更新已有记录
    else:
        from person import Person               #在该键值下生成/保存新纪录
        record = Person(name='?', age='?')
        newrecord = True      
    for field in fieldnames:
        #eval:字符串必须用引号引起来，否则出错
        setattr(record,field,eval(entries[field].get())) 
    db[key] = record
    if newrecord:
        showinfo(title='Notice' ,message='Insert a new record!')
    else:
        showinfo(title='Notice' ,message='Record Updated!')
    

db = shelve.open(shelvename)
window = makeWidgets()
window.mainloop()
db.close()

        
        
        
        
