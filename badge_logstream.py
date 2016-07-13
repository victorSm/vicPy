
import json, anydbm
from datetime import datetime
db = anydbm.open('badge_log','c')
while True:
	inline = raw_input('Swipe or X...')
	if inline == 'x':
	    db.close()
	    break
	inline = inline.lower()
	inline = inline.strip('c:')
	badge = str(float.fromhex(inline))
	timestamp = str(datetime.now())
	jString = json.dumps({"badge_number":badge, "datecode":timestamp})
	db[jString]='log_entry'

