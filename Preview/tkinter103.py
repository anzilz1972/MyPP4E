#coding=utf-8
'''
Created on 2017年6月7日

@author: 王国安
'''
from tkinter import *
from tkinter.messagebox import showinfo

def reply(name):
    showinfo(title='Reply', message='hello {}!'.format(name))

top = Tk()
top.title('Echo')
#top.iconbitmap('py-blue-trans-out.ico')

Label(top, text='Enter you name:').pack(side=TOP)
ent = Entry(top)
ent.pack(side=TOP)
btn = Button(top, text='Submit', command=(lambda: reply(ent.get())))
btn.pack(side=RIGHT)

top.mainloop()
