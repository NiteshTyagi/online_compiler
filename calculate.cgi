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



    
def data():
    d=cgi.FieldStorage()
    return (d.getvalue('code'),d.getvalue('select'),d.getvalue('input'))

if __name__=="__main__":
    try:
        htmltop()
        #db,cursor=connectdb()
        a=data()
        #people=displaydb(db,cursor,a[0])[0][2:]
        code=a[0]
        option=a[1]
        input=a[2]
        #print(code,option,input)
        url='https://api.jdoodle.com/v1/execute'
        request_object={
                'clientId': "59751131d6528d7512116c9aefc54cbe",
                'clientSecret':"15e9f4b6723aa7272e9875857595137df5df93235d3b5cd6f697d64fcc0292d7",
                'script' : code,
                'stdin':input,
                'language':option,
                'versionIndex': "2",
            };
        headers={'content-type':'application/json'}
        data=requests.post(url,data=json.dumps(request_object),headers=headers)
        result=eval(data.text)

        print(result['output'].strip(),end='$')   #Actual output
        print(result['memory'],end='$')
        print(result['cpuTime'],end='$')
    except:
        cgi.print_exception()
