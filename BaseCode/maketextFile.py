#! /usr/bin/python

#filename makeTextFile.py

import os
ls = os.linesep

#getfilename
while True:

	if os.path.exists(fname):
		print "Error: '%s' already exists " %fname
	else:
		break

#get file content(text) lines
all = []
print "\nEnter lines('.'by itself to quit).\n"

#loop until user terminates input
while True:
	entry = raw_input('>')
	if entry == '.':
		break
	else:
		all.append(entry)

#wtrite lines to file with proper line-end
fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()
print 'Done'
