#!/usr/bin/python

import cgi
import sys
#get username from c & store it to usrname
usrname = sys.argv[0]

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
    				</div>"""

htmlTail = """</body>
		</html>"""

#form to fill out when update the status
htmlForm = """<div class="updatespace">
        		<h1>Update.</h1>
        		<form name="statusupdate" action="cgi_bin/status.py usrname">
            		<textarea name="update"  placeholder="What's hogging your processors today?"> </textarea>
        			<button type="submit" value=" "/> 
        			<h2>COMMIT</h2>
    			</form>
       		</div>"""

htmlUpdate = """<div class="dashspace">
        <div class="dashhead">
            <h1>UpToDate.</h1>
        </div>
    
        <div class="friendupdate">
            <div class="friendusername">sham</div>
            <div class="friendstatus">Hey guys it's Sham here just testing out this dashboard lol!!!!!!!! </div>            
        </div>
        
        <div class="friendupdate">
            <div class="friendusername">justin bieber</div>
            <div class="friendstatus">IS IT 2L8 NOW 2 SAY SORRRRRRYYYYYYYYY </div>       
        </div>
        
         <div class="friendupdate">
            <div class="friendusername">justin trudeau</div>
            <div class="friendstatus">obama told me I'm a total OG and I was like 'ain't it truuuuuu-doe (get it? because my last name is trudeau.) </div>       
        </div>
        
         <div class="friendupdate">
            <div class="friendusername">joseph vybihal</div>
            <div class="friendstatus">stuff lol</div>       
        </div>
        
         <div class="friendupdate">
            <div class="friendusername">PRINCE OF NIGERIA</div>
            <div class="friendstatus">PLEASE DEPOSIT $200 INTO MY OVERSEAS BANKING ACCOUNT. I WILL BE VERY GRATEFUL.</div>       
        </div>
        
         <div class="friendupdate">
            <div class="friendusername">sham</div>
            <div class="friendstatus">yo I hate my life rn hahahahahahhaaa</div>       
        </div>
    </div> """

       		
if __name__ == "__main__":
	try:
		#open the html files
	    html = open("index.html","w")

	except:
		cgi.print_exception()

#append html code to index.html 
html.write(htmlTop)
html.write(htmlForm)
html.write(htmlTail)
html.write(htmlUpdate)
#close the file
html.close()	

	
	
	