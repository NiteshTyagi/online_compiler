#!C:\Users\nites\AppData\Local\Programs\Python\Python37-32\python.exe

import cgi
import mysql.connector as conn
import json
import requests

def htmltop():
    print("""Content-type:text/html\n\n
    <!DOCTYPE html>
    <html lang='en'>
    <head>
       <meta charset='utf-8'/>
       <title>MY First server-side template</title>
       </head>
       <body>""")

def htmltail():
    print("""</body>
    </html>    
    """)

    
def getdata():
    file=cgi.FieldStorage()
    firstname=file.getvalue("Firstname")
    lastname=file.getvalue('lastname')
    email=file.getvalue('emailaddress')
    birthday=file.getvalue('bday')
    return [firstname,lastname,email,birthday]

if __name__=="__main__":
    try:
        htmltop()
        data=getdata()
        for i in data:
          print(i,"</br>")
        htmltail()
    except:
        cgi.print_exception()
