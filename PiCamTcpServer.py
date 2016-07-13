import socket
import time
import picamera
import sys
import datetime
import os

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('', 8001)
server_socket.bind(server_address)
print >> sys.stderr, ''
print >> sys.stderr, 'starting up on %s port %s' % server_socket.getsockname()
server_socket.listen(1)


print >> sys.stderr, ''
print >> sys.stderr,'Listening'
while True:
	connection, client_address = server_socket.accept()
	
	print >> sys.stderr, ''
	print >> sys.stderr, 'client connected:', client_address
	try:
		
		
		sys.path.insert(0, "usr/bin/raspistill")
		utc_datetime = datetime.datetime.utcnow()
		strTimestamp=utc_datetime.strftime("%Y.%m.%d_%H.%M.%S")
		filename = '/IMAGES/IMG_' + strTimestamp + '.jpg'

		print >> sys.stderr, ''
		print >> sys.stderr, 'CAPTURING IMAGE'
		def still():
			os.system('raspistill -vs -n -awb tungsten -q 100 -mm backlit -t 10 -o ' + filename)
		still() 
		print >> sys.stderr, ''
		print >> sys.stderr, 'DONE GETTING IMAGE'
		
		#-----------------------------------------------------------------------------------------------------------
		while True:
			data = connection.recv(1024)
			if data:
				print >> sys.stderr, ''
				print >> sys.stderr, 'received "%s"' % data
				connection.sendall(data)
			else:
				break
		#-----------------------------------------------------------------------------------------------------------
		print >> sys.stderr, 'Sent message'
	except:
		print >> sys.stderr, ''
		print >> sys.stderr, '********************************************************************'
		print >> sys.stderr, '********* THERE WAS AN ERROR BEFORE CLOSING CONNECTION! ************'
		print >> sys.stderr, '********************************************************************'
	finally:
		try:
			print >> sys.stderr, ''
			print >> sys.stderr, 'connection is going to be closed'
			connection.close()
			# server_socket.close()
			print >> sys.stderr, ''
			print >> sys.stderr, 'connection is closed'
			print >> sys.stderr, ''
		except:
			print >> sys.stderr, ''
			print >> sys.stderr, '**************************************************************'
			print >> sys.stderr, '********* THERE WAS AN ERROR CLOSING CONNECTIONS! ************'
			print >> sys.stderr, '**************************************************************'
		