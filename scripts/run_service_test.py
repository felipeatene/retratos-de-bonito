from app.schemas.person_link import LinkPersonToPhotoRequest
from app.services.person_link_service import add_person_to_photo
from app.database import SessionLocal
import sqlite3, os

# pick a photo id from DB
DB = 'retratos.db'
print('DB:', os.path.abspath(DB))
con = sqlite3.connect(DB)
cur = con.cursor()
cur.execute('SELECT id FROM photos LIMIT 1')
row = cur.fetchone()
if not row:
    print('No photo found')
    raise SystemExit(1)
photo_id = row[0]
print('Using photo_id', photo_id)

payload = LinkPersonToPhotoRequest(
    full_name='Maria Atene',
    nickname='Dona Maria',
    birth_year=1948,
    role='retratado'
)

with SessionLocal() as db:
    res = add_person_to_photo(db, photo_id, payload)
    print(res)
