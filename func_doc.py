#!/usr/bin/python
#Filename:func_doc.py

def getMax(x, y):
	'''We can get the max number.
	
	this is the code about get max number.'''

	x = int(x)
	y = int(y)

	if (x > y):
		print 'The max number is', x
	else:
		print 'The max number is', y

print getMax.__doc__
getMax(7, 8)

