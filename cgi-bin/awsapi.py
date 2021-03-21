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
     #output = sp.getoutput("sudo aws ec2 create-key-pair --key-name {}".format(key))
     output = output + "\n\nkey pair created"

elif choice == "2":
  #output = sp.getoutput('sudo aws ec2 create-security-group --group-name {} --description "SG Created using webapp. {}"'.format(sg,Type)
  output  = output + "\n\n<b> security group created </b>"
   
elif choice == "3":
   #output = sp.getoutput("sudo aws ec2 authorize-security-group-ingress --group-name {} --protocol {} --port {} --cidr {}/0".format(sg,protocol,port,ip))
   output = output + "\n\n<b> Added inbound rules. </b>"
   
elif choice == "4":
   # name = "--tag-specifications " + '"ResourceType = instance , Tags = [{Key=\"Name\",Value=\"' + name +'"}]"'
   # az = "--placement " + '"AvailabilityZone='+ az + '"'
   # output = sp.getoutput("sudo aws ec2 run-instances --image-id {0} --instance-type {1} --key-name {2} --security-group-ids {3}  {4} {5}".format(image,Type,key,sg,name,az))
   output= output + "\n\n<b> Instance Launched </br>"
   
elif choice == "5":
   #  output = sp.getoutput('sudo aws ec2 create-volume --availability-zone "{}" --size {}'.format(volume,size))
   output = output + "\n\n<b> Ebs volume created </b>"
   
elif choice == "6":
   #  output = sp.getoutput("sudo aws ec2 attach-volume --instance-id {} --volume-id {} --device {}".format(iid,vid,volume))
   output = output + "\n\n<b> EBS volume attached to instance </b>"
   
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
       

