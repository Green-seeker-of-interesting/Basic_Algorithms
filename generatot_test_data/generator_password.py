from random import choice

def generatorPassword(len_password: int =16, using_simvols: tuple = (True, True, True , True) ) -> str:
    """
    Генератор поролей. Принимает длинну необходимого пароля и  кортеж с флагами 
    len_password - Длинна будующего пароля
    using_simvols - настройки генератора 
        1 - Чиста
        2 - Строчные буквы 
        3 - Заглавные буквы
        4 - Спец символы
    """
    # Проверили что пользователь оставил нам хоть один вариант для генерации пароля 
    if sum(using_simvols) == 0:
        return "Error using_simvols full False"

    numeric_s = "1234567890"
    lower_case_s = "abcdefghijklmnopqrstuvwxyz"
    upper_case_s = "ABCDEFZHIKLMNOPQRSTVX" 
    special_symbols_s = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"


    big_case_s = ""
    if using_simvols[0] : big_case_s += numeric_s
    if using_simvols[1] : big_case_s += lower_case_s
    if using_simvols[2] : big_case_s += upper_case_s
    if using_simvols[3] : big_case_s += special_symbols_s

    password_string_out = ""
    # Дополнителная проверка что пароль точно отвечает требованиям 
    while not passwordValidator(password=password_string_out, using_simvols=using_simvols):
        password_string_out = ""
        for i in range(len_password):
            password_string_out += choice(big_case_s)

    return password_string_out

def passwordValidator(password : str ,using_simvols:tuple = (True, True, True , True), minimal_len_password = 8) -> bool:
    """
    Валидатор пароля
    Принимает пароль и информацию о символах которые он должен содержат.
    Возвращает булевое знаечние. True если все условия хорошего пороля выполнены 
        using_simvols - настройки  
        1 - Чиста
        2 - Строчные буквы 
        3 - Заглавные буквы
        4 - Спец символы
    """
    total_flag = True

    numeric_s = "1234567890"
    lower_case_s = "abcdefghijklmnopqrstuvwxyz"
    upper_case_s = "ABCDEFZHIKLMNOPQRSTVX" 
    special_symbols_s = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

    if len(password) < minimal_len_password: total_flag = False
    if using_simvols[0] and not checkingMatchingCharInStrings(numeric_s, password): total_flag = False
    if using_simvols[1] and not checkingMatchingCharInStrings(lower_case_s, password): total_flag = False
    if using_simvols[2] and not checkingMatchingCharInStrings(upper_case_s, password): total_flag = False
    if using_simvols[3] and not checkingMatchingCharInStrings(special_symbols_s, password): total_flag = False

    return total_flag


def checkingMatchingCharInStrings(arg_1:str, arg_2:str) -> bool:
    """Проверяет есть ли между строками хотябы один общий элемент"""
    return not(set(arg_1).isdisjoint(set(arg_2))) 