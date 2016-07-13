import json, anydbm
from datetime import datetime
from bottle import get, put, run, template

@get('/')
def reqHandle():
  rfdb = anydbm.open('badge_log','r')
  tp = template('Data Entry: {{data}}', data = rfdb.keys())
  rfdb.close()
  return tp
	
run (host='10.232.166.144', port=8000, debug=True)
