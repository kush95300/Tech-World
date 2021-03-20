#! /usr/bin/python3

print("content-type: text/html")
print()


import cgi
import subprocess as sp
db = cgi.FieldStorage()

choice = db.getvalue("choice")
key = db.getvalue("key")

sg = db.getvalue("sg")
Type=db.getvalue("Type")

protocol = db.getvalue("protocol")
ip = db.getvalue("ip")
port = db.getvalue("port")

name = db.getvalue("name")
az=  db.getvalue("az")

volume= db.getvalue("volume")
size = db.getvalue("size")

vid = db.getvalue("vid")
iid= db.getvalue("iid")

image = db.getvalue("image")

output="" 
if choice =="1" :
     output = "key pair created"

elif choice == "2":
  
  output  = "security group created"
   
elif choice == "3":
   output = "Add inbound rules"
   
elif choice == "4":
   output= "Instance launched"
   
elif choice == "5":
   output = "Ebs volume created"
   
elif choice == "6":
   output = "EBS volume attached to instance"
   
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
       

