#! /usr/bin/python
#filename:using_tuple.py

zoo = ('wolf', 'elephant', 'penguin')
print 'Number of animals in the zoo is ', len(zoo)

new_zoo = ('monkey', 'dolphin', zoo)
print 'Numer of animals in the zoo is ', len(new_zoo)
print 'All animals in the new zoo are', new_zoo
print 'Animal brought from old zoo are', new_zoo[2]
print 'Last animal brought from old zoo is', new_zoo[1][2]
