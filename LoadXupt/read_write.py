#! /usr/bin/python
#coding=utf-8

import word_to_pinyin as convert
import codecs

# filename:read_wrote.py

def get_name():
	info = codecs.open('result.txt', 'r', 'utf-8')
	for name_info in info:
		#print (name_info)
		result = convert.Get_pinyin(name_info)
		write_name(result)
		#write_name("中文输入测试")
def write_name(word):
	result_name = codecs.open('pinyin_result.txt', 'a', 'utf-8')
	result_name.write(word)

if __name__ == '__main__':
	get_name()
