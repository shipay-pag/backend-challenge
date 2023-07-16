from passlib.context import CryptContext
import random
import string


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def generate_random_password(length=8):
    """
    Gera uma senha aleatória com o comprimento especificado.

    Args:
        length (int): O comprimento da senha. O padrão é 8.

    Returns:
        str: A senha aleatória gerada.

    """
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))


def hash_password(password: str):
    """
    Criptografa uma senha utilizando o contexto definido.

    Args:
        password (str): A senha a ser criptografada.

    Returns:
        str: A senha criptografada.

    """
    return pwd_context.hash(password)
