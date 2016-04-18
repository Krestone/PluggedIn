#!/usr/bin/python

import cgi

form=cgi.FieldStorage()

usrname=form.getvalue("username")
friends=[]
for key in form.keys():
 friends.append( form.getvalue(key) )
 
with open('users.txt', 'r+b') as f:
    lines = f.readlines()
    for i in xrange(0, len(lines)-1,4 ):
        if lines[i].startswith(usrname):
           for friend in friends:
              if friend not in lines[i]: 
                lines[i]= lines[i].strip() + ' '  + friend + '\n' 
    f.seek(0)
    for line in lines:
     f.write(line)





htmlTop="""Content-type:text/html\n\n
<html>
	<head>
		<link rel="stylesheet" href="../dashboard.css">
		<title>PluggedIn - dashboard</title>
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

htmlForms="""
<center><h1></br></br></br></br></br>FRIENDS ADDED!</h1></center>
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
""" % (usrname, usrname, usrname)

htmlBottom="""
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



</body></html>"""

print htmlTop+htmlForms+htmlBottom
