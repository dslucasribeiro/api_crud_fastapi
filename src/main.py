from fastapi import FastAPI  # Importa a classe FastAPI do framework FastAPI.
from fastapi.middleware.cors import CORSMiddleware
from .router import router  # Importa o objeto 'router' do módulo 'router' local.

app = FastAPI()  # Cria uma instância do aplicativo FastAPI.
# 'app' é a instância central do seu aplicativo web.
origins = ["http://localhost:4200"]  # Adicione a URL do seu frontend

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)  # Anexa o roteador 'router' ao aplicativo FastAPI.
# Isso registra todas as rotas e operações definidas em 'router' no aplicativo.
