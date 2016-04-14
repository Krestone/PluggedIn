#!/usr/bin/python
import os
import cgi
import sys


#test = raw_input("status:")
#create a file to store the status input
temp_file = open("temp_file.txt", "w")

#get input
form = cgi.FieldStorage()

usrname= form.getvalue("username")
statusupdate=form.getvalue("update")

'''print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello</title>"
print "</head>"
print "<body>"
print "<h2> %s </h2>" % statusupdate
print "<h2> %s </h2>" % usrname
print "</body>"
print "</html>"'''


#write input to the txt file
#temp_file.write(test)
temp_file.write(statusupdate)

#close file
temp_file.close()



#store lines in file to a list -> because the status is restricted to one line, if there's
#more than one line, it's easier to get rid of it.
with open("temp_file.txt") as f:
	temp = f.readlines()

#if input is not empty, store status 
if temp:
	statusline = "\n" + usrname + " " + temp[0] 
	status_file = open("status.txt", "a")
	status_file.write(statusline)
	status_file.close()


	
	

