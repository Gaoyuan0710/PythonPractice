#! /usr/bin/python
#simple Server - charter 1 - server.py

import socket

host = ''
port  = 51423

s = socket.socket(socket.AF_INET, socket.SOCKET_STREAM)
s.setsockopt(socket.SOCKET, socket.SO_REUSEADDR)
s.bind((host, port))
s.listen(1)

print "Server is running on port %d; press Ctrl-C to terminate." %port

while 1:
	clientsocket, clientaddr = s.accept()
	clientfile = clientsock.makefile('rw', 0)
	clientfile.write("Welcome, " + str(clientaddr) + "\n")
	clientfile.write("Please enter a string:")
	line = clientfile.readline().strip()
	clientfile.wtrte("You entered %d characters.\n" %len(len))
	clientfile.close()
	clientsock.close()
