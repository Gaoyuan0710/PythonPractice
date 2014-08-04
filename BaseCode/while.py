#!/usr/bin/python
#filename: while.py

number = 23;
running = True

while running:
	guess = int(raw_input('Please intput integer:'))

	if guess == number:
		print 'Congratulations, you guessed it'
		running = False
	elif guess < number:
		print 'No, it is a little highter than that'
	else:
		print 'No, it is a little lower than that'
else:
	print 'The while loop is over.'
print 'Done'
