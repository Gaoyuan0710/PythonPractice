#! /usr/bin/pythin
#filename:using_list.py

shopList = ['apple', 'mango', 'carrot', 'banana']

print 'I have', len(shopList), 'items to purchase'

print 'These items are'
for item in shopList:
	print item,

print '\nI alse have to buy one rice'
shopList.append('rice')
print 'My shopping list is now', shopList

print 'I will sort my list now'
shopList.sort()
print 'Sorted shopping list is', shopList

print 'The first item I will buy this is', shopList[0]
oldList = shopList[0]
del shopList[0]
print 'I bought the ', oldList
print 'My shopping list is now', shopList

