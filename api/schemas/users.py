from pydantic import BaseModel


class UserCreate(BaseModel):
    """
    Classe responsável pelo modelo de Schema para criação de usuário.
    """
    name: str
    email: str
    role: int
    password: str = None
