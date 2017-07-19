#coding=utf-8
'''
Created on 2017年6月6日

@author: 王国安
'''

"""
person类的替代实现，包含数据、行为、和运算符重载（未用于对象的持久存储）
"""

class Person:
    """
          一般person：数据+逻辑
    """
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age  = age
        self.pay  = pay
        self.job  = job
    
    def lastName(self):
        return self.name.split()[-1]
    
    def giveRaise(self,percent):
        self.pay *= (1.0+percent)
        
    def __str__(self):
        return '<{} => {}, {}, {}, {}>'.format(self.__class__.__name__, self.name, \
                                   self.age,self.pay,self.job)
        
class Manager(Person):
    """
          带有自定义加薪的person
          继承了通用的lastName,str
    """
    def __init__(self,name,age,pay):
        Person.__init__(self,name,age,pay,'manager')
        
    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self,percent + bonus)

if __name__ =='__main__':
    bob = Person('Bob Smith', 42, 30000, 'software')
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    tom = Manager(name='Tom Doe' ,age=50, pay=50000)
    print(sue, sue.pay,sue.lastName())
    for obj in (bob,sue,tom):
        obj.giveRaise(0.10)      #调用该对象的giveRaise方法
        print(obj)               #调用通常的__str__方法


        
        

