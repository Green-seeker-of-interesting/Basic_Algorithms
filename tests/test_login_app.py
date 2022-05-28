import unittest
from generatot_test_data import generatorMailsAndPasswords, generatorMaPaWithHesh
from login_app import *
import os
from pandas import DataFrame

class TetsAuthorizationInterface(unittest.TestCase):

    def setUp(self) -> None:
        self.test_interfeise_main = authorizationInterface()
        self.test_interfeise_main.user_login = "main"
        self.test_interfeise_main.user_password = "1234"
        return super().setUp()

    #Проверка работы валидатора 
    def test_login_validator_true(self):
        self.assertTrue(self.test_interfeise_main.loginValidator("wuliw.ru@mail.ru"))

    def test_login_validator_false(self):
        self.assertFalse(self.test_interfeise_main.loginValidator("mail.ru"))

    #Проверка обязательных атрибутов 
    def test_get_input_data(self):
        self.assertIsInstance(self.test_interfeise_main.getInputData(),tuple)
        self.assertEqual(self.test_interfeise_main.getInputData(),("main", "1234"))

    def test_main_worker_interfeise(self):
        self.assertFalse(self.test_interfeise_main.mainWorker())


class TestAuthorizationCore(unittest.TestCase):

    def setUp(self) -> None:
        interfeise = authorizationInterface()
        self.core = authorizationCore(interfeise, "test_database.db")
        #Cсгенерировать тут тестовые данные и залить их в базу. 
        self.test_list_users = generatorMaPaWithHesh(generatorMailsAndPasswords(number_new_records=10,is_sorted=True))
        df = DataFrame(self.test_list_users, columns=["email", "hesh", "open_password"])
        self.core.db.saveDataFrame(df,tabel_name="test_1")      
        return super().setUp()

    def tearDown(self) -> None:
        os.remove("test_database.db")
        return super().tearDown()

    #Проверка что метод есть и к нему можно обратиться 
    def test_data_init_core(self):
        self.assertFalse(self.core.authorization_interface.mainWorker())

    # Проверка работы бинарного поиска. Возможно стоит разнести но пока не буду. 
    def test_binary_serch(self):
        test_list = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(self.core.binary_search(test_list,2),1)
        self.assertEqual(self.core.binary_search(test_list,9), len(test_list) - 1)
        self.assertIsNone(self.core.binary_search(test_list,-1))

    #тест основного воркера ядра
    def test_main_worker_authorization_core(self):
        self.core.authorization_interface.user_login = self.test_list_users[1][0] # берём логин из списка
        self.core.authorization_interface.user_password = self.test_list_users[1][2]# берём его открытиый пароль
        self.assertTrue(self.core.mainWorker(name_tabel="test_1"))

    def test_main_worker_authorization_core_bad_password(self):
        self.core.authorization_interface.user_login = self.test_list_users[1][0] # берём логин из списка
        self.core.authorization_interface.user_password = "12345"
        self.assertFalse(self.core.mainWorker(name_tabel="test_1"))

    def test_main_worker_authorization_core_bad_login(self):
        self.core.authorization_interface.user_login = "wuliw.ru@mail.ru"
        self.core.authorization_interface.user_password = self.test_list_users[1][2]
        self.assertFalse(self.core.mainWorker(name_tabel="test_1"))
