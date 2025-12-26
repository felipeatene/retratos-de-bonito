from fastapi.testclient import TestClient
from app.main import app
import sqlite3

DB = 'retratos.db'
con = sqlite3.connect(DB)
cur = con.cursor()
cur.execute('SELECT id FROM people LIMIT 1')
row = cur.fetchone()
if not row:
    print('No person found')
    raise SystemExit(1)
person_id = row[0]
print('Testing person_id', person_id)

client = TestClient(app)
resp = client.get(f'/people/{person_id}/photos')
print('Status', resp.status_code)
print(resp.json())
