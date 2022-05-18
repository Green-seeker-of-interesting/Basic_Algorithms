from faker import Faker
from .generator_password import generatorPassword


def generatorMailsAndPasswords(number_new_records: int , is_sorted: bool = False) -> list:
    """Создаёт пары почта-пороль. На вход принимает длинну будующей последовательности и необходимость сортировки"""
    fake = Faker()
    list_new_records = []
    for i in range(number_new_records):
        list_new_records.append((fake.unique.ascii_free_email(), generatorPassword(len_password=10)))

    #Если необходимо сортируем почты по алфавиту
    if is_sorted:
        list_new_records.sort(key=lambda x: x[0])

    return list_new_records
