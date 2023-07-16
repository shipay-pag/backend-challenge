"""
Este trecho de código define a classe `RoleReposiotry`, que fornece métodos para acessar e manipular dados de roles no banco de dados.

Classe:
    RoleRepository: Classe que encapsula operações relacionadas as roles no banco de dados.
"""
from api.database.session import DBSessionContext
from api.database.models import Role
from api.helpers.helpers import obj_to_dict


class RoleRepository(DBSessionContext):
    def get_role_by_id(self, role_id: int) -> dict:
        """
        Retorna um papel (role) com base no seu ID.

        Args:
            role_id (int): O ID do papel (role).

        Returns:
            dict: Dicionário contendo os dados do papel (role).

        Raises:
            None
        """
        with self.get_session_scope() as session:
            role = session.query(Role).filter(Role.id == role_id).first()
            return obj_to_dict(role) if role else None
