#!/usr/bin/python 

import cgi 
import sys 
import re 

form=cgi.FieldStorage()
# get the username from the hidden field

usrname=form.getvalue("username")
friend=form.getvalue("friend")
#read the txt line by line into info[]
with open("users.txt") as f:
	info = f.readlines()
	
i=0
#search through info for friend
while (i < (len(info)-3)):
	if (info[i].split(' ', 1)[0] == friend):
		fullname = info[i+2]
		jobdescription = info[i+3]
		break
	i = i + 1
		

htmlTop = """Content-type:text/html\n\n
<html>
	<head>
	    <link rel="stylesheet" href="friendprofile.css">
	    <title>PluggedIn - make friends</title>
	</head>
	    
	<body> 

	    <div class="topmenu">
			<a href=javascript:launchDash()>Dashboard</a> &emsp;&emsp;&emsp;&emsp;
			<a href="javascript:launchMake()">Make a friend</a> &emsp;&emsp;&emsp;&emsp;
			<a href="javascript:launchSee()">See a friend</a>  &emsp;&emsp;&emsp;&emsp; 
			<div class="logout">
				<a href="http://www.cs.mcgill.ca/~ycukra/PluggedIn/home/">Logout</a></div>
	    </div> """


htmlTop+= """	    
	    <div class="content">
	        <div class="header"><h1><i>import</i> </br> &emsp;&emsp;%s.info</h1></div> <!-- friend's username -->
	        <div class="userinfo">FULL_NAME: </br>
	        &emsp;&emsp; %s  </br></br></br> <!-- friend's full name --> 
	    JOB_DESCRIPTION: </br>
	    &emsp;&emsp;%s <!--friend's job description --> 
	        </div>
	    </div>
	    
	    <form name="statusupdate" action="http://www.cs.mcgill.ca/~ycukra/cgi-bin/status.py" method="get">
	        <input type="hidden" name = "update" value="">
	        <input type="hidden" name = "username" value="%s"> <!-- logged in user's username -->
	    </form>

	    <form name="makefriend" action="http://cs.mcgill.ca/~shossa15/cgi-bin/makefriends.py" method="get">
				<input type="hidden" name = "username" value="%s"> <!-- logged in user's username --> 
			</form>

			<form name="seefriend" action="http://www.cs.mcgill.ca/~ycukra/cgi-bin/seefriends.cgi" method="get">
				<input type="hidden" name = "username" value="%s"> <!-- logged in user's username --> 
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
</html>""" % (friend, fullname, jobdescription, usrname, usrname, usrname)
