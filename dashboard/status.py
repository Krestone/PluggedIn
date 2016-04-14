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

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello</title>"
print "</head>"
print "<body>"
print "<h2> %s </h2>" % statusupdate
print "<h2> %s </h2>" % usrname
print "</body>"
print "</html>"


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


#Dashboard

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


htmlDefaultStatus = """<div class="friendupdate">
            <div class="friendusername">SYSTEM</div>
            <div class="friendstatus">No recent status from your friends. OMG your friends are so quiet. GO AND MAKE NEW FRIENDS!!!</div>            
        </div> \n"""

html = open("index.html","a")
  
def update( status_list, i ):
	temp = status_list[i]
	html.write("""<div class="friendupdate">
		<div class="friendusername">""")
	#split the first word, i.e. username, from status, and store it to splited
	splited = temp.split(None, 1)
    #username: first index of splited
	html.write(splited[0])
	html.write("""</div> <div class="friendstatus">""")
    #status: second part of splited = status
	html.write(splited[1])
	html.write("""</div>
		</div> \n""")

#main program       		
if __name__ == "__main__":
	try:
		#open the html files
	    html = open("index.html","a")

	except:
		cgi.print_exception()

	#open the status.txt
	with open("status.txt") as f:
		status_list = f.readlines()

	if len(status_list) != 0:
		if len(status_list) >= 20:
			num = 20
		elif len(status_list) < 20:
			num = len(status_list)
		i=num
		while (i != 0):
			update(status_list, i)
			i=i-1      		
	#if there's no recent status, then just show default status
	else:
		html.write(htmlDefaultStatus)
		
	#close the file
	f.close()
	html.close()	

	
	
################################################# END OF QI'S CODE 	

html=open("index.html", "a")
htmlTail = """		
		</div>

		<script>
			function dash() {

			}

			function launchMake() {

			}

			function launchSee() {

			}
		</script>	
	</body>
</html>"""
html.write(htmlTail)
html.close()

	
	

