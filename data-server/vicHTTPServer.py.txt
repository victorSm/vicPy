import SocketServer, SimpleHTTPServer

class TCPSERVER(SocketServer.TCPServer):
	allow_reuse_address=True

	
handler = SimpleHTTPServer.SimpleHTTPRequestHandler

server = TCPSERVER(('10.232.166.235',8000),handler)

server.serve_forever()
