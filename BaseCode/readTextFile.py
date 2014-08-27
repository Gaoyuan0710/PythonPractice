#! /usr/bin/python
#Filename readTextFile.py

#get filename
fname = raw_input('Enter filename:')

print

#attempt to open file for reading

try:
	fobj = open(fname, 'r')
except IOEerror, e:
	print "*** file %s open error" %s, e
else:
	#display content to the screen

	for eachline in fobj:
		print eachline,
	fobj.close()
