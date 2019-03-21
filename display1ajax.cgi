#!C:\Users\nites\AppData\Local\Programs\Python\Python37-32\python.exe

import cgi
import mysql.connector as conn
import json
import requests

def htmltop():
    print("""Content-type:text/html\n\n
    """)

def htmltail():
    print("""</body>
    </html>    
    """)

def connectdb():
    db=conn.connect(host='localhost',user='root',passwd='',db='virtuallab')
    cursor=db.cursor()
    return db,cursor

def displaydb(db,cursor,a):
    sql='select * from virtual where id='+str(a)
    cursor.execute(sql)
    people=cursor.fetchall()
    return people
    
def data():
    d=cgi.FieldStorage()
    return (d.getvalue('fname'),d.getvalue('code'),d.getvalue('select'))

if __name__=="__main__":
    try:
        htmltop()
        result=[]
        db,cursor=connectdb()
        a=data()
        people=displaydb(db,cursor,a[0])[0][2:]
        code=a[1]
        option=a[2]
        #print(code,a[2])
        print(str(people[0]),end="$")  #excepted output 
        print(str(people[1]),end="$")  #excepted output
        print(str(people[2]),end="$")  #excepted output
        print(str(people[3]),end="$")  #input
        print(str(people[4]),end="$")  #input
        print(str(people[5]),end="$")  #input
        url='https://api.jdoodle.com/v1/execute'
        for i in range(3,6):
            request_object={
                'clientId': "59751131d6528d7512116c9aefc54cbe",
                'clientSecret':"15e9f4b6723aa7272e9875857595137df5df93235d3b5cd6f697d64fcc0292d7",
                'script' : code,
                'stdin':str(people[i]),
                'language':option,
                'versionIndex': "2",
            };
            headers={'content-type':'application/json'}
            data=requests.post(url,data=json.dumps(request_object),headers=headers)
            result.append(eval(data.text)['output'])
            #print(eval(data.text)['output'])   #Actual output
        print(result[0],end="$")
        print(result[1],end="$")
        print(result[2],end="$")
    except:
        cgi.print_exception()
