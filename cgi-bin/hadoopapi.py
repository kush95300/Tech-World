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
ip= db.getvalue("ip")

output="" 
if choice =="1" :
     # ansible role
     output = "node created"

elif choice == "2":
  # output = sp.getoutput("sudo hadoop dfsadmin -report | less")
  output  = "Report created"
   
elif choice == "3":
   output = "<a href='http://{}:50070'><b> Click here to Open </b></a>".format(ip)
   
elif choice == "4":
    #if fold == None:
    #   fold = ""
    #output = sp.getoutput("sudo hadoop fs -ls /{}".format(fold))
   output= "listed"
   
elif choice == "5":
   # output = sp.getoutput("sudo hadoop fs -cat /{}".format(file))
   output = "Hii , I am file"
   
elif choice == "6":
   # output = sp.getoutput("sudo hadoop fs -mkdir /{}".format(fold))
   output = "folder Created"
elif choice == "7":

   output = "File Created"
elif choice == "8":
    # if fold == None:
    #        output = sp.getoutput("sudo hadoop fs -touchz /{}".format(file))
    # else:
    #        output = sp.getoutput("sudo hadoop fs -touchz /{}/{}".format(fold,file))
   output = "Empty file created"
elif choice == "9":
# output = sp.getoutput("sudo hadoop fs -rm /{}/{}".format(fold,file))
   output = "File removed"

elif choice == "10":
# output = sp.getoutput("sudo hadoop fs -rmr /{}".format(fold))
   output = "folder removed"
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
       

