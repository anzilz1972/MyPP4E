#coding=utf-8
'''
Created on 2017年6月9日
@author: 王国安
实现用来查看和更新保存在shelve中类实例的基于web的界面；
shelve保存在服务器上（如果是本地机器的化，就是同一个机器）
'''

import cgi, shelve, sys, os                      # cgi.test()转储输入
global fieldnames

def htmlize(oldDict):
    newDict = oldDict.copy()
    for field in fieldnames:                        # 值可能包含&,>等字符   
        value = newDict[field]                      # 作为代码显示：被引号引起
        newDict[field] = cgi.escape(repr(value))    # 转移HTML字符
    return newDict

def fetchRecord(db,form):
    try:
        key = form['key'].value
        record = db[key]
        fields = record.__dict__                     #使用属性字典
        fields['key'] = key
    except:
        fields = dict.fromkeys(fieldnames,'?')
        fields['key'] = 'Missing or invalid key!'
    return fields

def updateRecord(db,form):
    if not 'key' in form:
        fields = dict.fromkeys(fieldnames,'?')
        fields['key'] = 'Missing key input!'
    else:
        key = form['key'].value
        if key in db:
            record = db[key]
        else:
            from person import Person
            record = Person(name='?', age='?')
        for field in fieldnames:
            setattr(record,field,eval(form[field].value))
        db[key] = record
        fields = record.__dict__
        fields['key'] = key
    return fields

def formatReplyhtml():
    # 主html模板
    rplyhtml = '''
    <html>
    <title>People Input Form</title>
    <body>
    <form method=POST action="peoplecgi.py">
        <table>
        <tr><th>key<td><input type=text name=key value="{key}">
        $ROWS$
        </table>
    
    <p>
        <input type=submit value="Fetch", name=action>
        <input type=submit value="Update", name=action>
    </form>
    </body>
    </html>
    ''' 
    # 为$ROWS$的数据行插入html
    rowhtml1 = '<tr><th>{}<td><input type=text name={} value=\"'
    rowhtml2 = '{}'
    rowshtml = ''
    
    for fieldname in fieldnames:
        rowshtml += (rowhtml1.format(fieldname,fieldname) + '{'+ rowhtml2.format(fieldname) + '}\">\n') 
    rplyhtml = rplyhtml.replace('$ROWS$', rowshtml)
    return rplyhtml

if __name__ =='__main__':                            #debug模式  
    fieldnames = ('name', 'age', 'job', 'pay')
    replyhtml = formatReplyhtml()
    print(replyhtml)

    shelvename = 'class-shelve'                      # shelve文件在当前工作目录    
    db =shelve.open(shelvename)
    for key in db:
        record = db[key]
        newdict = htmlize(record.__dict__)
        print('key==>{}\n\t\tOld Dict==>{}\n\t\tNew Dict==>{}'.format(key,record.__dict__,newdict))
    db.close()
    
    newdict['key'] = 'key'
    replyhtml = replyhtml.format(**newdict)
    print(replyhtml)
    
else:                                                #作为CGI服务程序，正常运行模式 
    fieldnames = ('name', 'age', 'job', 'pay')
    replyhtml = formatReplyhtml()

    form =cgi.FieldStorage()                         # 解析表单数据
    print('Content-type:text/html')                  # 响应html的header和空行
    sys.path.insert(0,os.getcwd())                   # 
    action = form['action'].value if 'action' in form else None

    shelvename = 'class-shelve'                      # shelve文件在当前工作目录    
    db =shelve.open(shelvename)
    if action == 'Fetch':
        fields = fetchRecord(db,form)
    elif action =='Update':
        fields = updateRecord(db,form)
    else:
        fields =dict.fromkeys(fieldnames,'?')
        fields['key'] = 'Missing or invalid action!'
    db.close()
    
    newdict = htmlize(fields)
    replyhtml = replyhtml.format(**newdict)
    print(replyhtml)
    
        





























