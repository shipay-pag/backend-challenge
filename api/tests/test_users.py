"""
Este arquivo contém testes para a API de usuários.

Os testes são realizados usando a biblioteca pytest e o cliente de teste TestClient do FastAPI.

Módulos requeridos:
    - pytest
    - fastapi.testclient
    - faker

Atributos:
    - app (FastAPI): Instância do aplicativo FastAPI.
    - client (TestClient): Cliente de teste para enviar solicitações HTTP à API.
    - faker (Faker): Instância do Faker para gerar dados falsos.
    - user_repository (UserRepository): Instância do repositório de usuários.

Fixtures: (A Fixture é um método que é executado antes de cada teste e pode ser reutilizado em vários testes)
    - test_user: Fixture para obter um usuário de teste existente ou criar um novo usuário antes de cada teste.

Testes:
    - test_create_user: Testa a criação de um novo usuário.
    - test_create_user_duplicate_email: Testa a criação de um usuário com um email já registrado.
    - test_get_user_role: Testa a obtenção do papel (role) de um usuário.
    - test_get_user_role_not_found: Testa a obtenção do papel (role) de um usuário não encontrado.
    - test_health_check: Testa a rota de verificação de integridade (health check).
"""
import pytest
from fastapi.testclient import TestClient
from faker import Faker
from api.main import app
from api.repositories.user_repository import UserRepository
from api.repositories.role_repository import RoleRepository
from api.schemas.users import UserCreate

repository = UserRepository()

client = TestClient(app)

faker = Faker()
user_repository = UserRepository()


@pytest.fixture
def test_user() -> dict:
    user = user_repository.get_random_user()

    if not user:
        new_user = UserCreate(
            name=faker.name(),
            email=faker.email(),
            role=1
        )
        user_repository.create_user(new_user)
        user = user_repository.get_random_user()

    return user


def test_create_user():
    response = client.post("/users/", json={"name": faker.name(), "email": faker.email(), "role": 1})
    assert response.status_code == 200
    assert response.json() == {"message": "User created successfully"}


def test_create_user_duplicate_email(test_user):
    filtered_user = {key:value for key, value in test_user.items() if key in ['name', 'email']}
    filtered_user['role'] = 1

    response = client.post("/users/", json=filtered_user)
    assert response.status_code == 400
    assert response.json() == {"detail": "Email already registered"}


def test_get_user_role(test_user):
    response = client.get(f"/users/{test_user.get('id')}/role")
    role = RoleRepository().get_role_by_id(test_user.get('role_id'))
    assert response.status_code == 200
    assert response.json() == {"role_description": role.get('description')}


def test_get_user_role_not_found():
    response = client.get("/users/999999/role")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}


def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "alive"}
