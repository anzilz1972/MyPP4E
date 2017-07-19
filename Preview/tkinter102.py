#coding=utf-8
'''
Created on 2017年6月7日

@author: 王国安
'''
from tkinter import *
from tkinter.messagebox import showinfo


class MyGui(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        button1 = Button(self, text='press', command=self.reply1)
        button1.pack(side=TOP)
        button2 = Button(self, text='press', command=self.reply2)
        button2.pack(side=BOTTOM)
    
    def reply1(self):
        showinfo(title='popup', message='Button 1 pressed!')
    def reply2(self):
        showinfo(title='popup', message='Button 2 pressed!')

if __name__ == '__main__':
    window = MyGui()
    window.pack()
    window.mainloop()
    