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
        <link rel="stylesheet"  type="text/css" href="style.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js" type="text/javascript"></script>
       <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
<style>
        #first,#second,#thrid{
            display: inline-block;
        border: 2px solid; 
        text-align: center;
        background-color: rgb(219, 210, 240);
        overflow-y: auto;
        margin-left: 7vw;
    }    
    </style>
<script language='javascript'>
        function setTip()
        {
            var x = document.getElementById("inlineFormCustomSelectPref").value;
            
           if ( x =='c' )
             document.getElementById("codearea").innerHTML=`/******************************************************************************

Welcome to Virtual lab Compiler.
Virtual lab Compiler is an online compiler  for C, C++, Python, Java, Ruby, Perl,
C#, VB, Swift.
Code, Compile, Run  online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int main()
{
    printf("Hello World");

    return 0;
}
`;
       
           else if ( x =='cpp' )
             document.getElementById("codearea").innerHTML=`/******************************************************************************

Welcome to Virtual lab Compiler.
Virtual lab Compiler is an online compiler  for C, C++, Python, Java, Ruby, Perl,
C#, VB, Swift.
Code, Compile, Run  online from anywhere in world.

*******************************************************************************/
#include <iostream>
using namespace std;

int main(){
    string name;
    
    // read the user's name from standard input
    cin >> name;
    
   // output the name along with 'Hello' String
    cout << "Hello " << name << endl;
    
    return 0;
}

// Just Click on SUBMIT to run the code`;
       
           else if ( x =='java' )
             document.getElementById("codearea").innerHTML=`/******************************************************************************

Welcome to Virtual lab Compiler.
Virtual lab Compiler is an online compiler  for C, C++, Python, Java, Ruby, Perl,
C#, VB, Swift.
Code, Compile, Run  online from anywhere in world.

*******************************************************************************/
public class Main
{
	public static void main(String[] args) {
		System.out.println("Hello World");
	}
}
`;

            else if(x=='python3')
            document.getElementById("codearea").innerHTML=`'''

Welcome to Virtual lab Compiler.
Virtual lab Compiler is an online compiler  for C, C++, Python, Java, Ruby, Perl,
C#, VB, Swift.
Code, Compile, Run  online from anywhere in world.

'''
# print the name along with Hello
print 'Hello %s' % name

# Just click on SUBMIT to run the code`;

            else if(x=='perl')
            document.getElementById("codearea").innerHTML=`'''

Welcome to Virtual lab Compiler.
Virtual lab Compiler is an online compiler  for C, C++, Python, Java, Ruby, Perl,
C#, VB, Swift.
Code, Compile, Run  online from anywhere in world.

'''
print ('Hello World')`;

            else if(x=='ruby')
            document.getElementById("codearea").innerHTML=`=begin

Welcome to Virtual lab Compiler.
Virtual lab Compiler is an online compiler  for C, C++, Python, Java, Ruby, Perl,
C#, VB, Swift.
Code, Compile, Run  online from anywhere in world.

=end
=cut
print "Hello World";
`;

            else if(x=='csharp')
            document.getElementById("codearea").innerHTML=`=begin

Welcome to Virtual lab Compiler.
Virtual lab Compiler is an online compiler  for C, C++, Python, Java, Ruby, Perl,
C#, VB, Swift.
Code, Compile, Run  online from anywhere in world.

=end
puts "Hello World"
`;

            else if(x=='go')
            document.getElementById("codearea").innerHTML=`(comment "
;; Sample code to perform I/O:

(def x (read-line))                 ; Reading input from STDIN
(println (str "Hi, " x "."))        ; Writing output to STDOUT

;; Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
")

; Write your code here
`;

             else if(x=='vbn')
            document.getElementById("codearea").innerHTML=`/******************************************************************************

Welcome to Virtual lab Compiler.
Virtual lab Compiler is an online compiler  for C, C++, Python, Java, Ruby, Perl,
C#, VB, Swift.
Code, Compile, Run  online from anywhere in world.

*******************************************************************************/
using System;
class HelloWorld {
  static void Main() {
    Console.WriteLine("Hello World");
  }
}
`;

             else if(x=='swift')
            document.getElementById("codearea").innerHTML=`/*
// Sample code to perform I/O:

fmt.Scanf("%s", &myname)            // Reading input from STDIN
fmt.Println("Hello", myname)        // Writing output to STDOUT

// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
*/

// Write your code here
`;

             else
             {
            document.getElementById("codearea").innerHTML=``;
            alert('Please select Desired Langauage at least');
        }
        }
       </script>
 <script>
                var database; 
                var aa; 
                var inputtestcase=[];
                var outputtestcase=[];
                var actualresult=[];
                var section=['first','second','thrid'];

                $(document).ready(function ()
                {    
                   $("#Save").click(function () 
                    { 
                      var data1=document.getElementsByName("code")[0].value;
                      key= document.getElementById("Save").getAttribute("data-key");
                      var e = document.getElementById("inlineFormCustomSelectPref");
                      var strUser = (e.options[e.selectedIndex].value);
                      console.log(strUser);
                      loadDoc(key,data1,strUser);
                      function loadDoc(a,data1,strUser){
                      aa=a;
                      var xhttp = new XMLHttpRequest();
                      xhttp.onreadystatechange = function() {
                      if (this.readyState == 4 && this.status == 200) 
                        {
                          database =(this.responseText).split("$");
                          window.inputtestcase=[database[3],database[4],database[5]];
                          window.outputtestcase=[database[0],database[1],database[2]];
                          window.actualresult=[database[6],database[7],database[8]];
                          //console.log(actualresult.length);         
                           $.each(inputtestcase , function (index, value){
                              $("#"+section[index]).css("width","300px");
                              $("#"+section[index]).css("height", "150px");
                              $("#"+section[index]).html("<h4><u>TEST CASE &nbsp;&nbsp;"+(index+1)+"</u></h4><b style='text-align:left;'>INPUT</b>:&nbsp &nbsp"+inputtestcase[index].trim()+"<br></u></h4><b style='text-align:left;'>EXPECTED RESULT</b>:&nbsp &nbsp"+(outputtestcase[index]).trim()+"<br><b>YOUR RESULT:</b>&nbsp &nbsp"+(actualresult[index]).trim());     
                     
                           });
                        }
                    };
                      xhttp.open("POST", "display1ajax.cgi", true);
                      xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                      xhttp.send("fname="+a+'&code='+encodeURIComponent(data1)+'&select='+strUser);
                    };
                  });
                });
        </script> 
</head><style>
.card{
        border-style: outset;
        border-color: red;
        width:70vw;
        margin-left:10vw;
    }</style>
<body>
<div class="header">
                <a href="http://www.virtuallab1.tech/" class="logo">Virtual lab</a>
                <div class="header-right">
                  <a class="active" href="#home">Home</a>
                  <a href="#contact">About Us</a>
                  <a href="#contact">Blogs</a>
                  <a href="#contact">Courses</a>
                  <a href="#contact">Contact Us</a>
                  <a href="#about">Compile Section</a>
                </div>
              </div>""")


def htmltail():
    print("""</body>
    </html>    
    """)

def connectdb():
    db=conn.connect(host='localhost',user='root',passwd='',db='virtuallab')
    cursor=db.cursor()
    return db,cursor

def displaydb(db,cursor,valuefromform):
    sql='select * from virtual where id='+str(valuefromform)
    cursor.execute(sql)
    people=cursor.fetchall()
    return people


        

def  output(file,valuefromform):
    op=open(file)
    print("""<br><div class="card">
    <div class="card-body">""")
    readdata=op.read()
    print(readdata)
    print("""</div>
    </div>  <br><form class="form-block">
                <label class="my-1 mr-2" for="inlineFormCustomSelectPref"><h5 style="margin-left:5vw;">Select language</h5></label>
                <select class="custom-select my-1 mr-sm-2" id="inlineFormCustomSelectPref" onChange='setTip()'>
                  <option selected>Choose...</option>
                  <option value="c">C</option>
                  <option value="cpp">C++</option>
                  <option value="java">Java</option>
                  <option value="python3">Python</option>
                  <option value="perl">Perl</option>
                  <option value="ruby">Ruby</option>
                  <option value="csharp">C#</option>
                  <option value="go">GO</option>
                  <option value="vbn">VB.Net</option>
                  <option value="swift">Swift3</option>
                </select>
                <div class="input-group">
                        <div class="input-group-prepend">
                          <span class="input-group-text">With Coding<br> Playground</span>
                        </div>
                        <textarea  name="code" id="codearea" class="form-control" aria-label="With textarea" rows="13" cols="70"style="background-color: black;color:#fff;"></textarea>
                      </div><br>
                      <input type="button" id="Save"  class="btn btn-success" value="Run code" data-key="""+str(valuefromform)+""" /> 
                      </form>
                      
              <div id='first' style="white-space: pre-wrap;"></div>
                <div id="second" style="white-space: pre-wrap;"></div>
                <div id="thrid" style="white-space: pre-wrap;"></div>""")
    


        


def data():
    d=cgi.FieldStorage()
    if d.getvalue('firstSubmit')=='Solve it?=1':
        return '1'
    elif d.getvalue('secondSubmit')=='Solve it?=2':
        return '2'
    elif d.getvalue('thirdSubmit')=='Solve it?=3':
        return '3'
    elif d.getvalue('fourSubmit')=='Solve it?=4':
        return '4'
    elif d.getvalue('fiveSubmit')=='Solve it?=5':
        return '5'
    elif d.getvalue('sixSubmit')=='Solve it?=6':
        return '6'
    elif d.getvalue('sevenSubmit')=='Solve it?=7':
        return '7'
    elif d.getvalue('eightSubmit')=='Solve it?=8':
        return '8'
    else:
        return '9'
    

if __name__=="__main__":
    try:
        htmltop()
        db,cursor=connectdb()
        
        valuefromform=data()
        
        people=displaydb(db,cursor,valuefromform)
               
        output(people[0][1],valuefromform)                
        htmltail()
    except:
        cgi.print_exception()
