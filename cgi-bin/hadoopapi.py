#! /usr/bin/python3

print("content-type: text/html")
print()


import cgi
import subprocess as sp
db = cgi.FieldStorage()
#print(db)
choice = db.getvalue("choice")
fold = db.getvalue("fold")

file = db.getvalue("file")
content=db.getvalue("content")

node= db.getvalue("node")

output="" 
if choice =="1" :
     output = "node created"

elif choice == "2":
  
  output  = "Report created"
   
elif choice == "3":
   output = "Opened"
   
elif choice == "4":
   output= "listed"
   
elif choice == "5":
   output = "Hii , I am file"
   
elif choice == "6":
   output = "folder Created"
elif choice == "7":
   output = "File Created"
elif choice == "8":
   output = "Empty file created"
elif choice == "9":
   output = "File removed"

elif choice == "10":
   output = "folder removed"
elif choice == "11":
   output = "folder Created"
else:
   output = "Something went Wrong..."
print("""<style>
   body{
       background-color:rgb(0,0,0,0.8);
      text-align:center;
       justify-content:center;
     }
      pre{
        font-size: 20px;
        color:white;
      font-weight: bold;
      padding -top:0px
}
h1{
color : blue;
padding-bottom:0px;
}
</style>""")
print("""
<body>
<pre>
<h1 style = "">Output</h1>

{}
</pre>
</body>
""".format(output))
       

