import sqlite3
p = r'P:/Projetos/retratos-de-bonito/retratos.db'
conn = sqlite3.connect(p)
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
rows = cur.fetchall()
for r in rows:
    print(r[0])
conn.close()
