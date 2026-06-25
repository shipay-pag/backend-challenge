"""
Este trecho de código cria um aplicativo FastAPI que expõe uma API para manipulação de usuários.
Ele inclui um roteador de usuários e um endpoint para verificação de integridade (health check).

O aplicativo é iniciado usando o servidor ASGI Uvicorn.

Módulos requeridos:
    - fastapi
    - uvicorn

Exemplo de uso:
    $ uvicorn main:app --host=localhost --port=8003 --reload

Atributos:
    app (FastAPI): A instância do aplicativo FastAPI.

Rotas:
    - /users: Rota para manipulação de usuários.
    - /: Rota de verificação de integridade (health check).

"""
from fastapi import FastAPI, status
from api.routers import users


app = FastAPI()

app.include_router(users.router, prefix='/users', tags=['Users'])


@app.get("/", tags=['HealthCheck'], status_code=status.HTTP_200_OK)
async def health_check():
    """
    Endpoint para verificação de integridade do serviço.
    Retorna um JSON indicando que o serviço está em execução.

    Returns:
        dict: Dicionário contendo o status da verificação.
    """
    return {'status': 'alive'}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost",
                port=8003, reload=True)
