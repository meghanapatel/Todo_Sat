import json
from app.main import app

def test_home():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"Welcome" in response.data

def test_get_todos():
    response = app.test_client().get("/todos")
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) > 0
