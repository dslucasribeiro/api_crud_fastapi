from fastapi.testclient import TestClient


from src.main import app

client = TestClient(app)


def test_main_status_code():
    response = client.get("/")
    assert response.status_code == 200

def test_main_response():
    response = client.get("/")
    assert response.json() == {"Hello": "World"}

def test_listar_produtos():
    response = client.get("/produtos")
    assert response.status_code == 200
    
