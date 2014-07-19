while True:
	s = raw_input('Please input someting')
	if s == 'quit':
		break
	if len(s) < 3:
		continue
	print 'Input is of sufficient length'
