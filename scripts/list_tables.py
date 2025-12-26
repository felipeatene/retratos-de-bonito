import sqlite3
import os
import json

print(os.path.abspath('retratos.db'))
con = sqlite3.connect('retratos.db')
rows = [r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table'")]
print(json.dumps(rows, ensure_ascii=False))
