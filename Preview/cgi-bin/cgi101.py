#coding=utf-8
'''
Created on 2017年6月7日

@author: 王国安
'''
#!/usr/bin/python
import cgi
form = cgi.FieldStorage()
print('Content-type: text/html\n')
print('<title>Reply Page</title>')
if not 'user' in form:
    print('<h1>Who are you?</h1>')
else:
    print('<h1>Hello <i>{}</i></h1>'.format(cgi.escape(form['user'].value)))