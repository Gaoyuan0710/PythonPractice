#! /usr/bin/python
#coding=utf-8

import codecs

# filename:read_wrote.py

def get_name():
	info = codecs.open('name_list.txt', 'r', 'utf-8')
	for name_info in info:
		print (name_info)
		write_name(name_info)
		#write_name("中文输入测试")
def write_name(word):
	result_name = codecs.open('result.txt', 'a', 'utf-8')
	result_name.write(word)

if __name__ == '__main__':
	get_name()
