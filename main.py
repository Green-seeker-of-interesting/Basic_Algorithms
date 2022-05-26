from login_app import authorizationCore, authorizationInterfaceConsole
from setting import DATABASE_NAME, TABEL_USERS_NAME_FOR_LOGIN
#Фаил является общей точкой входа в систему и всегда используется при запуске. 



if __name__ == "__main__":
    print("Тестирование системы")
    interface = authorizationInterfaceConsole()
    core =  authorizationCore(interface, DATABASE_NAME)
    out = core.mainWorker(TABEL_USERS_NAME_FOR_LOGIN)
    print(out)


