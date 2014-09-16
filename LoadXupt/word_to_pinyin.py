#! /usr/bin/python
# -*-coding:utf-8-*-

def convert(ch):
    """该函数通过输入汉字返回其拼音，如果输入多个汉字，则返回第一个汉字拼音.
       如果输入数字字符串，或者输入英文字母，则返回其本身(英文字母如果为大写，转化为小写)
    """
    length = len('柯') #测试汉字占用字节数，utf-8，汉字占用3字节.bg2312，汉字占用2字节
    intord = ord(ch[0:1])
    if (intord >= 48 and intord <= 57):
        return ch[0:1]
    if (intord >= 65 and intord <=90 ) or (intord >= 97 and intord <=122):
        return ch[0:1].lower()
    ch = ch[0:length] #多个汉字只获取第一个
    with open(r'./convert-utf-8.txt') as f:
        for line in f:
            if ch in line:
#				print (line[length:len(line)-3])

                return line[length:len(line)-3]
def Get_pinyin(word):
	i = 0
	pinyin = ''
#	word = Myword.encode('utf-8')
	while i < len(word) / len('符'):
		simple_world = word.decode('utf-8')[i:i+1].encode('utf-8')
		print simple_world
#		simple_world = word[i:i+1].encode('utf-8')
		pinyin += convert(simple_world)
		i += 1
#	print pinyin
	return pinyin

#if __name__ == "__main__":
#	word = raw_input("Please input the word")
#	print (word)
#	print (Get_pinyin(word))
