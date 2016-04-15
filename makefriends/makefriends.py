#!/usr/bin/python 

import urllib2 

try: 
	USERS = urllib2.urlopen("http://www.cs.mcgill.ca/~ycukra/cgi-bin/users.txt")

except IOError: 
	print "Error opening user database! WHERE DID U PUT THE FILE"

else: 
	pass

# now initialize the html code 
html_code=""" 
<html>
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
    		<form name="checkusers" action="test.cgi" method="post"> <!-- action, method--> 
"""

currentuser=USERS.readline() # get username 

while currentuser!="":

	USERS.readline() # next line will be password, which we don't need 
	currentfullname=USERS.readline()
	USERS.readline() # next line will be job desc, which we don't need 

	# create checkbox 
	html_code += ("""
		<div class="check"><input type="checkbox" name="%s" value=""></div>
		""" % currentuser) 
	html_code += ("""
		<div class="username"><h2>%s</h2></div> 
		""" % currentuser)
	# append full name 
	html_code += ("""<div class="fullname"><h3>%s</h3></div>
		""" % currentfullname) 
	# line break 
	html_code += (""" </br>

		""")
	currentuser=USERS.readline() # now, get next username 

USERS.close() # close the file 



# finish HTML code 
html_code += """	
				<div class="submit"> 
					<button type="submit" value=" "/> 
				</div>
			</form>
		</div>
	</div>

    <form name="makefriend" action="MAKEFRIENDURL" method="get">
        <input type="hidden" name = "username" value="%s">
    </form>

    <form name="seefriend" action="www.cs.mcgill.ca/~ycukra/cgi-bin/seefriends.cgi" method="get">
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

try: 
	INDEX=open("index.html", "w")
except IOError: 
	print "Error writing to HTML file because I am stupid!!!!!!!"
else: 
	pass

INDEX.write(html_code)
INDEX.close()