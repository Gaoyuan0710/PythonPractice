#!/usr/bin/python
#filename :using_sys.py

import sys

print 'The command line are arguments are'
for i in sys.argv:
	print i

print '\n\n The PATHONPATH is', sys.path, '\n'
