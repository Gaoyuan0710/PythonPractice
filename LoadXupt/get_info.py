#!/usr/bin/python
#coding=utf-8
# Filename get_info.py

import codecs

def write_name(word):
	result_name = codecs.open('result.txt', 'a', 'utf-8')
	result_name.write(word)
def cut_1name():
	info = codecs.open('name_list.txt', 'r', 'utf-8')
	for name_info in info:
		print (name_info)
		result = name_info.split(' ')
		print (result[1].encode('utf8'))
		write_name(result[1])
		write_name('\r\n')
def cut_2name():
	info = codecs.open('name_list2.txt', 'r', 'utf-8')
	for name_info in info:
		print (name_info)
		result = name_info.split(' ')
		print (result[1].encode('utf8') + ' ' + result[4].encode('utf8'))
		write_name(result[1])
		write_name('\r\n')
		write_name(result[4])
if __name__ == '__main__':
	cut_1name()
	cut_2name()
