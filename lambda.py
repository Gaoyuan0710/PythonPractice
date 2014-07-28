#! /usr/bin/python
#filename:lambda.py

def make_repeater(n):
	return lambda s:s * n

test = make_repeater(2)

print test('nihao\n')
print test(3)
