from app.repositories.photo_repository import update_photo_curation
from app.database import SessionLocal
import sqlite3, os
from app.models.enums import PhotoStatus, Visibility

DB = 'retratos.db'
print('DB:', os.path.abspath(DB))
con = sqlite3.connect(DB)
cur = con.cursor()
cur.execute('SELECT id, status, visibility FROM photos LIMIT 1')
row = cur.fetchone()
if not row:
    print('No photo found')
    raise SystemExit(1)
photo_id, status_before, vis_before = row
print('photo', photo_id, 'before', status_before, vis_before)

with SessionLocal() as db:
    # carregar photo
    photo = db.query.__self__.bind  # dummy to keep code simple
    # instead, query
    from app.models.photo import Photo
    photo = db.query(Photo).filter(Photo.id==photo_id).first()
    res = update_photo_curation(db, photo=photo, status=PhotoStatus.CATALOGADA, visibility=Visibility.RESTRITA, curator_name='Felipe Atene')
    print('updated:', res.id, res.status, res.visibility)
