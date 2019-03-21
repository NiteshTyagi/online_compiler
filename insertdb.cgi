#!C:\Users\nites\AppData\Local\Programs\Python\Python37-32\python.exe
import cgi
import mysql.connector as conn
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
def connectDB():
     db=conn.connect(host='localhost',user='root',passwd="",db='virtuallab')
     cursor=db.cursor()
     return db,cursor

def data():
     url=[]
     #url.append(['C:\\\\xampp\\\\htdocs\\\\pythoncreatedb\\\\programs\\\\array-ds.html',"3 2 6 5","12 36 12 35 21","12 21 365 325 214 144","4\n 5 6 2 3","5\n 21 35 12 36 12","6\n 144 214 325 365 21 12"])
     #url.append(['C:\\\\xampp\\\\htdocs\\\\pythoncreatedb\\\\programs\\\\Arithmatic.html',"6","8","1","3\n3","4\n2","3\n2"])
     #url.append(['C:\\\\xampp\\\\htdocs\\\\pythoncreatedb\\\\programs\\\\loop.html',"0\n1\n4\n9\n16\n25","0\n1\n4\n9","0\n1\n4\n9\n16\n25\n36\n49","5","3","7"])
     url.append(['C:\\\\xampp\\\\htdocs\\\\pythoncreatedb\\\\programs\\\\helloworld.html',"Hello, World!","HELLO WORLD!","heLLo WoRlD!","Hello, World!","HELLO WORLD!","heLLo WoRlD!"])
     return url

def create(db,cursor):
     cursor.execute("""create table virtual(id int AUTO_INCREMENT PRIMARY KEY,dataurl VARCHAR(70) NOT NULL,
     testcase1 VARCHAR(30) NOT NULL,testcase2 VARCHAR(30) NOT NULL,testcase3 VARCHAR(30) NOT NULL,
     input1 VARCHAR(30) NOT NULL, input2 VARCHAR(30) NOT NULL,input3 VARCHAR(30) NOT NULL)""")
     db.commit()

def insert(db,url,cursor):
     for each in url:
          sql="insert into virtual (dataurl,testcase1,testcase2,testcase3,input1,input2,input3) values(%s,%s,%s,%s,%s,%s,%s)"
          val=tuple(each)
          cursor.execute(sql, val)
          db.commit()


if __name__=="__main__":
     try:
          htmltop()
          db,cursor=connectDB()
          #create(db,cursor)
          url=data()
          insert(db,url,cursor)
          htmltail()
     except:
          cgi.print_exception()
