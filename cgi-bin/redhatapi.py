#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi 

print('''<style>
pre{
color: black;
font-weight:bold;
font-size:20px
}
</style>

''')

db = cgi.FieldStorage()

cmd =db.getvalue("Command")
output=sp.getstatusoutput("sudo docker exec defaults "+cmd)
if output[0]!= 0:
    c=sp.getoutput("sudo docker start defaults")
    output=sp.getoutput("sudo docker exec defaults "+cmd)
else:
    output=output[1]

print("<body style='padding :40px;'>")
print('<h1 style ="color:#df405a;">Output</h1>')
print("<pre>{}</pre>".format(output))
print("</body>")
