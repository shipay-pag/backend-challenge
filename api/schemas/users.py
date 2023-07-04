from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    role: int
    password: str = None
