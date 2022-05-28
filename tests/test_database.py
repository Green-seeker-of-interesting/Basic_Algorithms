from os import remove
import unittest
from database import databaseWorker
from sqlite3 import Connection
from pandas import DataFrame


class TestDatabaseWorker(unittest.TestCase):

    NAME_DB = "test_db.sqlite"

    #Создание базы для теста 
    def setUp(self) -> None:
        self.db = databaseWorker(name_db=self.NAME_DB)
        return super().setUp()

    #Удаление базы 
    def tearDown(self) -> None:
        remove(self.NAME_DB)
        return super().tearDown()

    #Проверка что конектер создан
    def test_database_init(self):
        self.assertIsInstance(self.db.con, Connection)        

    def test_give_value_on_table(self):
        test_list = [1,2,3,4,5]
        df = DataFrame(test_list)
        local_name_teble = "tb_1"
        self.db.saveDataFrame(df, local_name_teble)
        value_from_db = self.db.giveValueOnTable(local_name_teble)
        self.assertEquals(test_list[1], value_from_db[1])

    # На всякий случай оставлю но тесты абсолютно одинаковые. ХЗ как их разнести.
    def test_save_datafreim(self):
        test_list = [1,2,3,4,5]
        df = DataFrame(test_list)
        local_name_teble = "tb_2"
        self.db.saveDataFrame(df, local_name_teble)
        value_from_db = self.db.giveValueOnTable(local_name_teble)
        self.assertEquals(test_list[1], value_from_db[1])
    