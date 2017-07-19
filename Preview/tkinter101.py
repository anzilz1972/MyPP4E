#coding=utf-8
'''
Created on 2017年6月7日

@author: 王国安
'''
from tkinter import *
from tkinter.messagebox import showinfo

def reply():
    showinfo(title='popup', message='Button Pressed!')
    
window = Tk()
button = Button(window, text='press', command=reply)
button.pack()
window.mainloop()