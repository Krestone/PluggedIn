#!/usr/bin/python

#http://cs.mcgill.ca/~shossa15/cgi-bin/makefriends.py?username=sham&sham="on"&bob="on"

import urllib2
import cgi 
import sys 
import re 

form=cgi.FieldStorage()
# get form and username 
usrname=form.getvalue("username")

# open the users.txt file 
try: 
	USERS = urllib2.urlopen("http://www.cs.mcgill.ca/~ycukra/cgi-bin/users.txt")

except IOError: 
	print "Error opening user database! WHERE DID U PUT THE FILE"

else: 
	pass


lines=USERS.readlines() 
# lines now in a list 
# seeking user 

i=0
currentuser=lines[0].split(' ',1)[0]
# just want the first word of the first line 
while currentuser!=usrname:
# while we haven't found the specific user 
	i = i+4
	# things are separated by full name, jobs, etc. 
	currentuser=lines[i].split(' ',1)[0]
	# update the line we are looking at


# now we have found the user we want to add friends for; whole line 
# is in lines[i]. 

# we get a bunch of people who may or may not be already on the list; 
# we don't add duplicates though

modify=lines[i]
# this is the string we'll be checking against 


	

