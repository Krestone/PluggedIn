#!/usr/bin/python

import urllib2
import cgi
import sys
import re

form=cgi.FieldStorage()
usrname=form.getvalue("username").strip()

htmlTop="""Content-type:text/html\n\n"""
htmlTop+="""<html>
	<head>
	    <link rel="stylesheet" href="./makefriends.css">
	    <title>PluggedIn - make friends</title>
	</head>
    
	<body> 
	    <div class="topmenu">
			<a href=javascript:launchDash()>Dashboard</a> &emsp;&emsp;&emsp;&emsp;
			<a href="javascript:launchMake()">Make a friend</a> &emsp;&emsp;&emsp;&emsp;
			<a href="javascript:launchSee()">See a friend</a>  &emsp;&emsp;&emsp;&emsp; 
			<div class="logout">
				<a href="http://www.cs.mcgill.ca/~ycukra/PluggedIn/home/">Logout</a></div>
	    </div> 

    <div class="content">
    	<div class="header"><h1>Connect.</h1> </div>
    	<div class="userlist">
    		<form name="checkusers" action="http://cs.mcgill.ca/~ycukra/cgi-bin/addfriend.py" method="get"> <!-- action, method--> 
    		<input type="hidden" name="username" value="%s">
""" % usrname
try: 
	USERS = urllib2.urlopen("http://www.cs.mcgill.ca/~ycukra/cgi-bin/users.txt","r")

except IOError: 
	print "Error opening user database! WHERE DID U PUT THE FILE"

else: 
	pass

allusers=USERS.readlines()
numusers=len(allusers)/4

for i in range(0,numusers):
	if allusers[i*4].split(' ',1)[0].strip() == usrname.strip():
	# here we are looking for the logged-in user's list of friends
		alreadyadded=allusers[i*4]
		# storing that user's list of friends 
		break
splitlist=alreadyadded.split(' ')

oldfriends=[]

for friend in splitlist:
	current = friend.replace('\n','').strip()
	oldfriends.append(current)

# make sure all whitespaces are gone, as well as newline chars

USERS.close()

index=0 # to keep track of users

for i in range(0,numusers):
	# get the username
	currentuser=allusers[index].split(' ',1)[0].strip(' ')
	currentuser=currentuser.replace("\n","")
	index=index+2 # move pointer
	# get the full name
	currentfullname=allusers[index]
	index=index+2 # move pointer again 
	# check if already added
	if currentuser in oldfriends:
		continue
	htmlTop+="""<div class="check"><input type="checkbox" name="%d" value="%s"></div>""" % (i,currentuser)
	htmlTop+="""<div class="username"><h2>%s</h2></div>""" % currentuser 
	htmlTop+="""<div class="fullname"><h3>%s</h3></div></br>""" % currentfullname
	
htmlTop+= """	
				<div class="submit"> 
					<button type="submit" value=" "/> 
				</div>
			</form>
		</div>
	</div>

    <form name="makefriend" action="http://www.cs.mcgill.ca/~shossa15/cgi-bin/makefriends.py" method="get">
        <input type="hidden" name = "username" value="%s">
    </form>

    <form name="seefriend" action="http://www.cs.mcgill.ca/~ycukra/cgi-bin/seefriends.cgi" method="get">
        <input type="hidden" name = "username" value="%s">
    </form>
    
    <form name="statusupdate" action="http://www.cs.mcgill.ca/~ycukra/cgi-bin/status.py" method="get">
        <input type="hidden" name = "update" value="">
        <input type="hidden" name = "username" value="%s">
    </form>

    <script>
        function launchDash() {
            document.forms["statusupdate"].submit();
        }

        function launchMake() {
            document.forms["makefriend"].submit();
        }

        function launchSee() {
            document.forms["seefriend"].submit();
        }
    </script>		
</body>

</html> """ % (usrname, usrname, usrname)

print (htmlTop)