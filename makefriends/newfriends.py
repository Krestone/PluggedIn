#!/usr/bin/python

#http://cs.mcgill.ca/~shossa15/cgi-bin/makefriends.py?username=sham&Hello+sham+python+Wildcookie%0D%0A=&sham+Hello+python%0D%0A=&test%0D%0A=

import cgi 
form=cgi.FieldStorage()

usrname=form.getvalue(username)
