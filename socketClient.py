import cStringIO, socket

host,port = '192.168.1.101',51200

while True:
  streamObj = cStringIO.StringIO()
  inline = raw_input('Swipe or X...')
  if inline == 'x':
    streamObj.close()
    break
  streamObj.write(input)
  data = streamObj.getvalue()
    
  try:
    sock = socket .socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,port))
    sock.sendall(data+'\n')
    
  finally: 
    print("Dump input...")
    print streamObj.getvalue()
    streamObj.close()
    sock.close()
