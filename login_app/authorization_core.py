from .authorization_interface import authorizationInterface
from database import databaseWorker
from password_worker import passwordEqualsHasher

class authorizationCore:
    """Модуль для организации входа в ситему"""
    def __init__(self, authorization_interface: authorizationInterface, databse_name: str) -> None:
        """
        На вход принимает любой клас унаследованный от авторизационного интерфейса
        Плюс имя базы данных
        """
        self.authorization_interface = authorization_interface
        self.db = databaseWorker(databse_name)

    def mainWorker(self, name_tabel:str) -> bool:
        """Принимает имя таблици с пользователями"""
        self.authorization_interface.mainWorker()
        all_users_from_db = self.db.giveValueOnTable(name_tabel)

        #Кастыль по изменению данных поскольку сохранялись и открытые пароли
        list_login_users = []
        list_password_users = []
        for entty in all_users_from_db:
            login, password, _ = entty
            list_login_users.append(login)
            list_password_users.append(int(password,16))

        #выполняю поиск. Инфа о логине пользователя в интерфейсе
        search_binary_finnish = self.binary_search(list_login_users, self.authorization_interface.user_login)

        if search_binary_finnish:
            # если нашли сверяем пароль 
            out_flag = passwordEqualsHasher(self.authorization_interface.user_password, list_password_users[search_binary_finnish])
        else:
            # Иначе такого логина нет 
            out_flag = False


        return out_flag


    def binary_search(self, array: list, element: str) -> int:
        """
        Бинарный поиск
        Вход массив и искомый элемент 
        Выход индекс если найден
        """
        top_element =  len(array) - 1
        down_element = 0

        while down_element <= top_element:
            mid_element = ((top_element - down_element) // 2) + down_element
            real_element = array[mid_element]
            if real_element == element:
                return mid_element
            elif real_element > element:
                top_element = mid_element-1
            else:
                down_element = mid_element+1


        return None
 
        

    