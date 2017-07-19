#coding=utf-8
'''
Created on 2017年6月6日

@author: 王国安
'''
from person import Person
class Manager(Person):
    def __init__(self,name,age,pay):
        Person.__init__(self,name,age,pay,'manager')
        
    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self,percent + bonus)
        
    #def giveRaise(self, percent, bonus=0.1):
    #    self.pay *= (1.0 + percent + bonus)

if __name__ == '__main__':
    tom = Manager(name='Tom Doe' ,age=50, pay=50000)
    print(tom.lastName())
    tom.giveRaise(0.20)
    print(tom.pay)
    print(tom)

