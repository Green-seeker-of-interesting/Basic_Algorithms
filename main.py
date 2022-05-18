from generatot_test_data import  generatorPassword, generatorMailsAndPasswords
 
#Фаил является общей точкой входа в систему и всегда используется при запуске. 



if __name__ == "__main__":
    print("Тестирование системы")
    mas =  generatorMailsAndPasswords(number_new_records=10, is_sorted=True)
    for i in mas:
        print(i)
        print("==========================")