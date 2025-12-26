from fastapi.testclient import TestClient
from app.main import app
import sqlite3

client = TestClient(app)
DB = 'retratos.db'
con = sqlite3.connect(DB)
cur = con.cursor()
cur.execute('SELECT id FROM photos LIMIT 1')
row = cur.fetchone()
if not row:
    print('No photo found')
    raise SystemExit(1)
photo_id = row[0]
print('photo', photo_id)

payload = {
    'title': 'Memória da praça',
    'content': 'Lembranças passadas oralmente pela família.',
    'author_name': 'Dona Maria',
    'author_relation': 'filha',
    'visibility': 'restrita'
}
client = TestClient(app)
resp = client.post(f'/stories/photos/{photo_id}', json=payload)
print('POST', resp.status_code, resp.json())
resp2 = client.get(f'/stories/photos/{photo_id}')
print('GET', resp2.status_code, resp2.json()[:2])
