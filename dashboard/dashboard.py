#!/usr/bin/python

import cgi
import sys
import re
#get username from c & store it to usrname
usrname = sys.argv[1]

html = open("index.html","w")

#store html code to Strings
htmlTop = """Content-type:text/html\n\n
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
    </div>"""
html.write(htmlTop)
html.close()



#form to fill out when update the status
html = open("index.html","a")
htmlForm = """
		<div class="updatespace">
    		<h1>Update.</h1>
    		<form name="statusupdate" action="http://www.cs.mcgill.ca/~ycukra/cgi-bin/status.py" method="get">
        		<textarea name="update" placeholder="What's hogging your processors today?"> </textarea>
    			<input type="hidden" name="username" value="%s">
    			<button type="submit" value=" "/> 
    			<h2>COMMIT</h2>
			</form>
   		</div> \n""" % usrname
html.write(htmlForm)
html.close()

html = open("index.html","a") 
htmlUpdate = """<div class="dashspace">
        <div class="dashhead">
            <h1>UpToDate.</h1>
        </div> \n"""
html.write(htmlUpdate)
html.close()
########################################## END OF SHAM'S CODE 


#open the friends.txt search for the line that contains username
friends = open("friends.txt", "r")
#initialize a list to store friends
usrfriend = []
for line in friends:
	#if first word of the line == username, then store it to usrfriend
	if line.split(' ', 1)[0] == usrname:
		#split string into list
		splitedline = line.split()
		#store it to usrfriend
		for user in splitedline:
			usrfriend.append(user)
		break
		
#print(usrfriend)
		
#open the status.txt
status = open("status.txt", "r")
#initialize a list to store relevant status
relevantsta = []

#search line by line to see the relevant status updated
for line in status:
	#if first word of the line == one of the friends, then store it to relevantsta
	for friend in usrfriend:
		if line.split(' ', 1)[0] == friend:
			relevantsta.append(line)
			
#print(relevantsta)

#check the numer of status
if len(relevantsta) >= 20:
	num = 20
elif len(relevantsta) < 20:
	num = len(relevantsta)

i = num-1
#initialize two list to store username and their status in parallel
usr = []
status = []
#from bottom to top through the list
while (i >= 0):
	#split the line 
	splited = relevantsta[i].split(None, 1)
	usr.append(splited[0])
	status.append(splited[1])	
	i = i-1

#print usr
#print status

html = open("index.html","a")
numsta = len(usr)
j=0
#print the html code
while (j < len(usr)):
	html.write("""<div class="friendupdate">
            <div class="friendusername">%s</div>
            <div class="friendstatus">%s</div>            
        </div> \n"""% (usr[j], status[j]))
	j = j+1
	
	
################################################# END OF QI'S CODE 	

html=open("index.html", "a")
htmlTail = """		
		</div>

		<form name="makefriend" action="MAKEFRIENDURL" method="get">
			<input type="hidden" name = "username" value="%s">
		</form>

		<form name="seefriend" action="SEEFRIENDURL" method="get">
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
</html>""" % usrname, usrname
html.write(htmlTail)
html.close()



