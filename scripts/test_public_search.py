from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
resp = client.get('/public/search')
print('Status', resp.status_code)
print(resp.json()[:5])
