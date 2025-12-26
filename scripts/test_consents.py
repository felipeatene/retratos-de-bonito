from fastapi.testclient import TestClient
from app.main import app
import sqlite3

client = TestClient(app)
DB = 'retratos.db'
con = sqlite3.connect(DB)
cur = con.cursor()
cur.execute('SELECT id FROM photos LIMIT 1')
photo = cur.fetchone()
cur.execute('SELECT id FROM people LIMIT 1')
person = cur.fetchone()
if not photo or not person:
    print('need photo and person in DB')
    raise SystemExit(1)
photo_id = photo[0]
person_id = person[0]
print('photo', photo_id, 'person', person_id)

# get existing
resp = client.get(f'/consents/photos/{photo_id}/people/{person_id}')
print('GET status', resp.status_code, resp.json())

# set consent
payload = {'consent_type':'publico','consent_date':'2025-12-25','notes':'autorizado'}
resp2 = client.post(f'/consents/photos/{photo_id}/people/{person_id}', json=payload)
print('POST status', resp2.status_code, resp2.json())

# get again
resp3 = client.get(f'/consents/photos/{photo_id}/people/{person_id}')
print('GET after', resp3.status_code, resp3.json())
