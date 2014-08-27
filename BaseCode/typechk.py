#! /usr/bin/python
#filename typechk.py

def displayNumType(num):
	print num , ' is ',
	if isinstance(num, (int, long ,float, complex)):
		print 'a number of type:', type(num).__name__
	else:
		print 'not a number at all'

while True:
	number = raw_input('Please input the number: ');

	if number == "quit":
		break;
	else:
		displayNumType(number)
