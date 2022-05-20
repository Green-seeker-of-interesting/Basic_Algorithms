
"""
Создал отдельный файл с интерфейсами. 
В теории могут быть разные способы получить данные:
    - консоль
    - http
    - ui
    - api
Так что будет присутствовать разные интерфейсы но имеющие один и тот же внешний апи
и уже этот интерфейс будет передоватся в ядро, общее для всех.
"""

class authorizationInterface:
    #Переменные в которые по умолчанию сохроняются данные 
    user_login = ""
    user_password = ""

    def mainWorker(self) -> bool:
        """Главный воркер интерфейса"""
        return False

    def getInputData(self) -> tuple:
        """Возвращает кортеж, введённый логин и пароль"""
        return (self.user_login , self.user_password)

    def loginValidator(self, login:str) -> bool:
        """Принимает введённый логин и выполняет его проверку"""
        return len(login) > 5 and "@" in login


class authorizationInterfaceConsole(authorizationInterface):

    def mainWorker(self) -> bool:
        self.inputLoginAndPassword()
        return True

    def inputLoginAndPassword(self):
        print("КУ!")
        
        while True:
            login = input("Введи свой логин плиз ->")
            if self.loginValidator(login=login):
                self.user_login = login
                break
            else:
                print("Что то пошло не так")

        self.user_password = input("Введите свой пароль плиз ->")


