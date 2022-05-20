from .authorization_interface import authorizationInterface


class authorizationCore:
    """Модуль для организации входа в ситему"""
    def __init__(self, authorization_interface: authorizationInterface) -> None:
        """На вход принимает любой клас унаследованный от авторизационного интерфейса"""
        self.authorization_interface = authorization_interface

    def mainWorker(self) -> bool:
        self.authorization_interface.mainWorker()
        
        return True

    