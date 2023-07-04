from passlib.context import CryptContext
import random
import string


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def generate_random_password(length=8):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))


def hash_password(password: str):
    return pwd_context.hash(password)
