#!E:\pythoninstall\python.exe

import cgi

def htmltop():
    print("""Content-type:text/html\n\n
    <!DOCTYPE html>
    <html lang='en'>
    <head>
       <meta charset='utf-8'/>
       <title>MY First server-side template</title>
       <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
       </head>
       <body>""")

def htmltail():
    print("""</body>
    </html>    
    """)
def getdata():
    file=cgi.FieldStorage()
    data=file.getvalue('user-message')
    return data

if __name__=="__main__":
    try:
        htmltop()
        data=getdata()
        print(''' <div class="col-lg-10">
                    <textarea name="user-message" id="user-message" class="form-control" cols="20" rows="10" placeholder="Enter your Message">''')
        print(data)
        print('''</textarea> 
                </div><!--end col 10-->
                <input type="submit" class="btn btn-primary" name='textarea' value='textarea'/>
              </div>''')
        htmltail()
    except:
        cgi.print_exception()
