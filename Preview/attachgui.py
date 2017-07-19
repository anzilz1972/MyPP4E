#coding=utf-8
'''
Created on 2017年6月7日

@author: 王国安
'''
from tkinter import *
from tkinter102 import MyGui

#应用主窗口
mainwin = Tk()
Label(mainwin, text=__name__).pack()

#弹出窗口
popup = Toplevel()                              #通过导入的程序创建
Label(popup, text='Attach').pack(side=LEFT)     #popup作为父容器 
MyGui(popup).pack(side=RIGHT)                   #popup作为父容器,附加myframe
mainwin.mainloop()