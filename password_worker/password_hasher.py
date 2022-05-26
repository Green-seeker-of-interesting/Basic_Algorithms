from hashlib import md5
from setting import SALT


def passwordHasher(password : str, using_salt : bool = True)-> int:
    """Принимает на вход пароль(str) а возвращает хеш"""
    if using_salt:
        out = md5(password.encode() + SALT).hexdigest()
    else:
        out = md5(password.encode()).hexdigest()
    return out


def passwordEqualsHasher(password : str, password_from_db : int) -> bool:
    """Сравнивает введённый пороль с солью в БД"""
    return int(passwordHasher(password=password, using_salt=True), 16) == password_from_db 