import cStringIO, socket

host,port = '192.168.1.101',51200
try:
  while True:
    streamObj = cStringIO.StringIO()
    
    inline = raw_input('Swipe or X...')
    if inline == 'x':
      streamObj.close()
      break

    inline = inline.lower()
    inline = inline.strip('c:')
    badge = str(float.fromhex(inline))
    badge = badge.strip('.0')

    streamObj.write(badge)
    data = streamObj.getvalue()
    
    try:
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      sock.connect((host,port))
      sock.sendall(data+'\n')
    except:
      print 'Socket connection error'
    
    finally: 
      print("Swiped badge number...")
      print streamObj.getvalue()
      streamObj.close()
      sock.close()
except:
  print 'End of line error'
  
finally:
  streamObj.close()
  sock.close()
  
