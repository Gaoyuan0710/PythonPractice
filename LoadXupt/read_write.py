#! /usr/bin/python
#coding=utf-8

import word_to_pinyin as convert
import codecs

# filename:read_wrote.py


def get_name():
	info = codecs.open('single_name.txt', 'r', 'utf-8')
	for name_info in info:
		print (name_info)

		result = convert.Get_pinyin(name_info.encode('utf-8'))
#		result = convert.Get_pinyin("测试版本")
		print result
		write_name(result)
		#all_name.append(name_info)
	info.close()
	#result = set(all_name)

	#for tmp in result:
	#	write_name(tmp)

def write_name(word):
	result_name = open('result.txt', 'a+')
	result_name.write('\n')
	result_name.write(word)
	result_name.close()

if __name__ == '__main__':
	get_name()
