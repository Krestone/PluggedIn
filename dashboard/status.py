#!/usr/bin/python

import cgi
import sys

usrname = sys.argv[0]
#test = raw_input("status:")
#create a file to store the status input
temp_file = open("temp_file.txt", "w")

#get input
form = cgi.FieldStorage()

#write input to the txt file
#temp_file.write(test)
temp_file.write(form.getvalue('update'))

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


	
	

