#! /usr/bin/python
#coding=utf-8

import word_to_pinyin as convert
import codecs

def main():
	output = open('final.txt', 'w')
	info = codecs.open('result.txt', 'r', 'utf-8')
	for name_info in info:
		print (name_info)
		result = convert.Get_pinyin(name_info.encode('utf-8'))
		print (result)
		output.write(result)
		output.write('\n')
	#result = convert.Get_pinyin("解决")
	#print (result)

if __name__ == '__main__':
	main()
