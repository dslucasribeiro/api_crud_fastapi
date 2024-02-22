from fastapi import FastAPI
from typing import List, Dict, Any
from schema import ProdutoSchema

app = FastAPI()

produtos: List[Dict[str, Any]] = [
    {
        "id": 1,
        "titulo": "Cadeira Gamer",
        "descricao": "Cadeira confortável para fazer live",
        "preço": 5.0,
    },
    {
        "id": 2,
        "a titulo": "Workshop",
        "descricao": "Workshop de deploy",
        "preço": 100.00,
    },
    {
        "id": 3,
        "a titulo": "Iphone",
        "descricao": "Iphone 14",
        "preço": None,
    },
]

id_atual = 3

@app.get("/")
def read_root():
    return {"Hello": "World"}

def lista(self):
    return self.produtos

def inserir(self, item: Dict[str, any]) -> Dict[str, any]:
    self.id_atual += 1
    item["id"] = self.id_atual
    return self.produtos.append(item)

@app.get("/produtos")
def listar_produtos():
    """
    View que que retorna o dicionário de produtos
    """
    return produtos

@app.get("/produtos/{produto_id}")
def listar_produto(produto_id: int):
    """
    View que retorna um produto específico
    """
    for produto in produtos:
        if produto["id"] == produto_id:
            return produto
    return {"Status": 404,"Mensagem": "Produto não encontrado"}