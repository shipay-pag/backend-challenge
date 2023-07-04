from api.database.session import DBSessionContext
from api.database.models import User
from api.helpers.helpers import obj_to_dict
from sqlalchemy.orm import joinedload


class UserRepository(DBSessionContext):
    def get_user_role(self, user_id) -> dict:
        with self.get_session_scope() as session:
            user = session.query(User).options(joinedload(User.role)
                                               ).filter(User.id == user_id).first()

            return obj_to_dict(user.role) if user.role else None

    def get_user_by_email(self, email) -> dict:
        with self.get_session_scope() as session:
            user = session.query(User).filter(User.email == email).first()

            return obj_to_dict(user) if user else None

    def create_user(self, user_data, hash_password) -> None:
        with self.get_session_scope() as session:
            user = User(
                name=user_data.name,
                email=user_data.email,
                password=hash_password,
                role_id=user_data.role
            )

            session.add(user)
