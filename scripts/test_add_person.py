import sqlite3
import os
import json
import urllib.request

DB = 'retratos.db'
print('DB path:', os.path.abspath(DB))
con = sqlite3.connect(DB)
cur = con.cursor()
cur.execute('SELECT id, file_name FROM photos LIMIT 1')
row = cur.fetchone()
if not row:
    print('No photos found in DB')
    raise SystemExit(1)
photo_id = row[0]
print('Using photo_id:', photo_id)

url = f'http://127.0.0.1:8000/photos/{photo_id}/people'
payload = {
    'full_name': 'Maria Atene',
    'nickname': 'Dona Maria',
    'birth_year': 1948,
    'role': 'retratado'
}
req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'})
with urllib.request.urlopen(req) as resp:
    print('Status:', resp.status)
    print(resp.read().decode())
