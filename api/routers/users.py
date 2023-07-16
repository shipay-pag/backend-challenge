from fastapi import APIRouter, HTTPException
from api.schemas.users import UserCreate
from api.helpers.password import generate_random_password, hash_password
from api.repositories.user_repository import UserRepository

router = APIRouter()

# Questão 3
@router.get('/{user_id}/role')
def get_user_role(user_id: int):
    """
    Retorna a descrição do papel (role) de um usuário com base no seu ID.

    Args:
        user_id (int): O ID do usuário.

    Returns:
        dict: Dicionário contendo a descrição do papel (role) do usuário.

    Raises:
        HTTPException(404): Se o usuário não for encontrado.
    """
    user_role = UserRepository().get_user_role(user_id)

    if not user_role:
        raise HTTPException(status_code=404, detail='User not found')

    return {'role_description': user_role.get('description')}


# Questão 4
@router.post('/')
def create_user(user_data: UserCreate):
    """
    Cria um novo usuário com os dados fornecidos.

    Args:
        user_data (UserCreate): Os dados do usuário a ser criado, com validação através do Schema.

    Returns:
        dict: Dicionário contendo uma mensagem de confirmação de que o usuário foi criado com sucesso.

    Raises:
        HTTPException(400): Se o email já estiver registrado.
    """
    existing_user = UserRepository().get_user_by_email(user_data.email)

    if existing_user:
        raise HTTPException(status_code=400, detail='Email already registered')

    # Gera uma senha aleatória se não for fornecida
    if not user_data.password:
        user_data.password = generate_random_password()

    # Criptografa a senha
    hashed_password = hash_password(user_data.password)

    UserRepository().create_user(user_data, hashed_password)

    return {'message': 'User created successfully'}
