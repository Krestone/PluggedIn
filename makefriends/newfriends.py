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


currentline=USERS.readline() # get username of first line 
currentuser=currentline.split(' ', 1)[0]
currentuser=currentuser.replace("\n","")
# we want to get rid of carriage returns 

# seeking user 
while currentuser!=usrname:
	USERS.readline() 
	USERS.readline() 
	USERS.readline() 
	currentline=USERS.readline() # skip four lines then read 
	currentuser=currentline.split(' ',1)[0]  
	currentuser=currentuser.replace("\n","")
	# keep track of the line, and the current user. 

# now we have found the user we want to add friends for; whole line 
# is stored in currentline. 

# we get a bunch of people who may or may not be already on the list; 
# we don't add duplicates though


if currentuser:
	

