#coding=utf-8
'''
Created on 2017年6月7日

@author: 王国安
'''
from tkinter import mainloop
from tkinter.messagebox import showinfo
from tkinter102 import MyGui

class CustomGui(MyGui):
    def reply1(self):
        showinfo(title='popup', message='I\'m Button 1!')
    def reply2(self):
        showinfo(title='popup', message='I\'m Button 2!')

if __name__ == '__main__':
    CustomGui().pack()
    mainloop()
    