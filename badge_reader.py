import cStringIO, json
from datetime import datetime


while True:
  index = open('/root/index.html','w')
  streamObj = cStringIO.StringIO()
  inline = raw_input('Swipe or X...')
  if inline == 'x':
    streamObj.close()
    index.close()
    break
  inline = inline.lower()
  inline = inline.strip('c:')
  badge = float.fromhex(inline)
  timestamp = str(datetime.now())
  json.dump([{"badge_number":badge, "timestamp":timestamp}],streamObj)
  print("Dump Json encoding...")
  print streamObj.getvalue()
  index.truncate()
  index.write(streamObj.getvalue())
  index.write('\n')
  streamObj.close()
  index.close()