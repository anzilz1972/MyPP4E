#coding=utf-8
'''
Created on 2017年6月19日

@author: 王国安
'''
def interact():
    print('Hello stream world')
    while True:
        try:
            reply = input('Enter a number>')
        except EOFError:
            break
        else:
            num = int(reply)
            print('{} squared is {}'.format(num,num ** 2))
    print('Bye')


if __name__ == '__main__':
    interact()