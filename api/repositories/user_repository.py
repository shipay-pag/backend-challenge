"""
Este trecho de código define a classe `UserRepository`, que fornece métodos para acessar e manipular dados de usuários no banco de dados.

Classe:
    UserRepository: Classe que encapsula operações relacionadas a usuários no banco de dados.
"""
from api.database.session import DBSessionContext
from api.database.models import User
from api.helpers.helpers import obj_to_dict
from sqlalchemy.orm import joinedload
from sqlalchemy.sql.expression import func


class UserRepository(DBSessionContext):
    def get_user_role(self, user_id: int) -> dict:
        """
        Obtém o papel (role) de um usuário com base no seu ID.
        """
        with self.get_session_scope() as session:
            user = session.query(User).options(joinedload(User.role)
                                               ).filter(User.id == user_id).first()

            return obj_to_dict(user.role) if getattr(user, 'role', None) else None

    def get_user_by_email(self, email: str) -> dict:
        """
        Obtém um usuário com base no seu email.
        """
        with self.get_session_scope() as session:
            user = session.query(User).filter(User.email == email).first()

            return obj_to_dict(user) if user else None

    def create_user(self, user_data, hash_password: str) -> None:
        """
        Cria um novo usuário no banco de dados.
        """
        with self.get_session_scope() as session:
            user = User(
                name=user_data.name,
                email=user_data.email,
                password=hash_password,
                role_id=user_data.role
            )

            session.add(user)

    def get_random_user(self) -> dict:
        """
        Obtém um usuário aleatório do banco de dados.
        """
        with self.get_session_scope() as session:
            user = session.query(User).order_by(func.random()).first()

            return obj_to_dict(user) if user else None
