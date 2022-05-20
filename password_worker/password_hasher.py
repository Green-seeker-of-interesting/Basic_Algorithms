from hashlib import md5
from setting import SALT


def passwordHasher(password : str, using_salt : bool = True)-> int:
    """Принимает на вход пароль(str) а возвращает хеш"""
    if using_salt:
        out = md5(password.encode() + SALT).hexdigest()
    else:
        out = md5(password.encode()).hexdigest()
    return out


def passwordEqualsHasher(pas_1 : str, pas_2 : str) -> bool:
    """Сравнивает два пароля"""
    return passwordHasher(pas_1) == passwordHasher(pas_2)