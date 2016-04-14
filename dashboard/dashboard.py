#!/usr/bin/python

import cgi
import sys
#get username from c & store it to usrname
usrname = sys.argv[1]

#store html code to Strings
htmlTop = """Content-type:text/html\n\n
			<html>
				<head>
    				<link rel="stylesheet" href="./dashboard.css">
    				<title>PluggedIn - dashboard</title>
				</head>
    
				<body>
    				<div class="topmenu">
        				<a href="dashboard">Dashboard</a> &emsp;&emsp;&emsp;&emsp;
        				<a href="makefriend">Make a friend</a> &emsp;&emsp;&emsp;&emsp;
        				<a href="seefriend">See a friend</a>  &emsp;&emsp;&emsp;&emsp; 
        				<div class="logout">
       					<a href="http://www.cs.mcgill.ca/~ycukra/PluggedIn/home/">Logout</a></div>
    				</div> \n"""

htmlTail = """		</div>
		</body>
	</html>"""

#form to fill out when update the status
htmlForm = """<div class="updatespace">
        		<h1>Update.</h1>
        		<form name="statusupdate" action="./status.py usrname">
            		<textarea name="update"  placeholder="What's hogging your processors today?"> </textarea>
        			<button type="submit" value=" "/> 
        			<h2>COMMIT</h2>
    			</form>
       		</div> \n"""

htmlUpdate = """<div class="dashspace">
        <div class="dashhead">
            <h1>UpToDate.</h1>
        </div> \n"""

htmlDefaultStatus = """<div class="friendupdate">
            <div class="friendusername">SYSTEM</div>
            <div class="friendstatus">No recent status from your friends. OMG your friends are so quiet. GO AND MAKE NEW FRIENDS!!!</div>            
        </div> \n"""
        
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
	    html = open("index.html","w")

	except:
		cgi.print_exception()

	#append html code to index.html 
	html.write(htmlTop)
	html.write(htmlForm)
	html.write(htmlUpdate)

	#open the status.txt
	with open("status.txt") as f:
		status_list = f.readlines()

	if len(status_list) != 0:
		if len(status_list) >= 20:
			num = 20
		elif len(status_list) < 20:
			num = len(status_list)
		i=0
		while (i < num):
			update(status_list, i)
			i=i+1      		
	#if there's no recent status, then just show default status
	else:
		html.write(htmlDefaultStatus)
		
	#append the last part of html code	
	html.write(htmlTail)
	#close the file
	f.close()
	html.close()	

	
	
	