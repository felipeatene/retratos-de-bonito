from fastapi.testclient import TestClient
from app.main import app
from app.schemas.photo_curation import CuratePhotoRequest
import sqlite3, os, json

DB = 'retratos.db'
con = sqlite3.connect(DB)
cur = con.cursor()
cur.execute('SELECT id FROM photos LIMIT 1')
row = cur.fetchone()
if not row:
    print('No photo found')
    raise SystemExit(1)
photo_id = row[0]
print('Testing photo_id', photo_id)

client = TestClient(app)

payload = {
    'status': 'catalogada',
    'visibility': 'restrita',
    'curator_name': 'Felipe Atene'
}
resp = client.patch(f'/photos/{photo_id}/curate', json=payload)
print('Status', resp.status_code)
print(resp.json())

# then update to validated/public
payload2 = {'status':'validada','visibility':'publica'}
resp2 = client.patch(f'/photos/{photo_id}/curate', json=payload2)
print('Status', resp2.status_code)
print(resp2.json())
