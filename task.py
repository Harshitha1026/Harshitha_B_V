#!/usr/bin/python3

print("content-type:text/html")
print()

import cgi
import subprocess
a = cgi.FieldStorage()
b = a.getvalue('x')

if ('Date' in b) or ('date' in b) or ('Show date' in b):
	value = subprocess.getoutput("date")
elif ('Calender' in b) or ('calender' in b) or ('cal' in b) or ('show calender' in b):
		value = subprocess.getoutput("cal")
elif ('list' in b) or ('List' in b) or ('folder' in b) or ('Folder' in b):
	value = subprocess.getoutput("ls")
elif ('path' in b) or ('Path' in b) or ('current' in b) or ('Current' in b) or ('directory' in b) or ('Directory' in b):
	value = subprocess.getoutput("pwd")

elif ('ip' in b) or ('IP' in b) or ('ip address' in b) or ('ifconfig'):
	add = subprocess.getoutput("ifconfig")
	print(add)
print(value)


