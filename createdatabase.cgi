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
     people=[]
     people.append(['nitesh','tyagi'])
     people.append(['Jyoti','tyagi'])
     people.append(['umesh','tyagi'])
     people.append(['saroj','tyagi'])
     people.append(['Abhishek','tyagi'])
     people.append(['shreya','tyagi'])
     people.append(['Aakansha','jain'])
     return people



def insert(db,people,cursor):
     for each in people:
          sql="insert into person (firstname,lastname) values('{0}','{1}')".format(each[0],each[1])
          cursor.execute(sql)
          db.commit()


if __name__=="__main__":
     try:
          htmltop()
          db,cursor=connectDB()
          cursor.execute("create table data())
          #people=data()
          #insert(db,people,cursor)
          htmltail()
     except:
          cgi.print_exception()
