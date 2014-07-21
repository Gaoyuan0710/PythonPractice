#! /usr/bin/python
#filename:using_dict.py

ab = {'swaroop' :'swaroop@163.com',
	'haha' :'haha@163.com',
	'nihao' :'nihao@164.com',
	'jingdong' :'jingdong@164.com'}

print "Swaroop's address is %s" %ab['swaroop']

ab['junjun'] = 'junjun@163.com'

del ab['nihao']

print '\nThere are %d contacts in the address-book\n' %len(ab)
for name, address in ab.items():
	print 'Contact %s at %s'%(name,address)

if 'jingdong' in ab:
	print"\n jingdong's address is %s"%ab['jingdong']
