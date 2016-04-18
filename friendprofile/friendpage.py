#!/usr/bin/python
import cgi
import sys
import re


#get form data

form=cgi.FieldStorage()
usrname=form.getvalue("username")
friend=form.getvalue("friend")

f=open("users.txt", "rU")
line=f.readline()

while (line.startswith(friend) == False):
  line=f.readline()

jobData=f.readline()
jobData=jobData.rstrip()


#store html code to Strings
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
    </div> 
"""    
htmlUserInfo="""<div class="content">
        <div class="header"><h1><i>import</i> </br> &emsp;&emsp;%s.info</h1></div>
        <div class="userinfo">FULL_NAME: </br>
        &emsp;&emsp; %s  </br></br></br>
    JOB_DESCRIPTION: </br>
    &emsp;&emsp;%s
        </div>
    </div>
""" % (friend, friend, jobData)    
htmlForms="""<form name="statusupdate" action="http://www.cs.mcgill.ca/~ycukra/cgi-bin/status.py" method="get">
        <input type="hidden" name = "update" value="">
        <input type="hidden" name = "username" value="%s">
    </form>

    <form name="makefriend" action="http://cs.mcgill.ca/~shossa15/cgi-bin/makefriends.py" method="get">
			<input type="hidden" name = "username" value="%s">
		</form>

		<form name="seefriend" action="http://www.cs.mcgill.ca/~ycukra/cgi-bin/seefriends.cgi" method="get">
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
    
    
</html>


""" % (usrname, usrname, usrname)

print htmlTop+htmlUserInfo+htmlForms
