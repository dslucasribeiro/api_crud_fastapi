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
    
def test_tamanho_lista():
    response = client.get("/produtos")
    assert len(response.json()) == 3

def test_pegar_produto():
    response = client.get("/produtos/1")
    assert response.json() == {
        "id": 1,
        "titulo": "Cadeira Gamer",
        "descricao": "Cadeira confortável para fazer live",
        "preço": 5.0,
    }