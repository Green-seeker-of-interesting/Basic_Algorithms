from login_app import authorizationCore, authorizationInterfaceConsole
from database import databaseWorker
#Фаил является общей точкой входа в систему и всегда используется при запуске. 



if __name__ == "__main__":
    print("Тестирование системы")
    # interface = authorizationInterfaceConsole()
    # core =  authorizationCore(interface)
    # core.mainWorker()
    data = databaseWorker("main_database.db")
    print(data.giveDfOnTable("bin_find"))

