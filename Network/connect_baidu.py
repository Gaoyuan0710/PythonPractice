#! /usr/bin/python
#filename:connect_baidu.py

import socket

print "Creating socket..."
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "done"

print "Connecting baidu..."
s.connect(("www.baidu.com", 80))
print "done"
