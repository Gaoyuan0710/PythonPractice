#!/usr/bin/python
#filename:deal_name.py

first_list = []

def deal_name():
	output = open('import.txt', 'r')
	input = open('result.txt', 'a+')
	for name in output:
		first_list.append(name)
	output.close()
	final_list = set(first_list)
	for tmp in final_list:
		input.write('\n')
		input.write(tmp)
	input.close()

if __name__ == '__main__':
	deal_name()
