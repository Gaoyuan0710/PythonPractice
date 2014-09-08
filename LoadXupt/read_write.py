#! /usr/bin/python
#coding=utf-8

import codecs

# filename:read_wrote.py

def get_name():
	info = codecs.open('name_list.txt', 'r', 'utf-8')
	result_name = codecs.open('result.txt', 'w+', 'utf-8')

	for name_info in info:
	#	write_name(name_info)
		print name_info.encode('utf-8'),
		result_name.write(name.decode('utf-8'))
def write_name(word):
	result_name = codecs.open('result.txt', 'w+', 'utf-8')
	print word.decode('utf-8')
	result_name.write(word.decode('utf-8'))

if __name__ == '__main__':
	get_name()

