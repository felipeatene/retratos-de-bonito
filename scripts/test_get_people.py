from fastapi.testclient import TestClient
from app.main import app
import sqlite3

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
resp = client.get(f'/photos/{photo_id}/people')
print('Status', resp.status_code)
print(resp.json())
