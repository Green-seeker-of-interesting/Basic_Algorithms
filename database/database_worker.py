import sqlite3
from pandas import DataFrame, read_sql

class databaseWorker:
    """Класс для взаимодействия с базой данных"""

    def __init__(self, name_db : str = 'sqlite_python.db') -> None:
        try:
            self.con = sqlite3.connect(name_db)
            #self.cursor = self.con.cursor()

        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)


    def saveDataFrame(self, data_for_save : DataFrame, tabel_name : str):
        """На вход принимает набор данных в виде DF и имя для будующей таблицы"""
        #!!!! Забить это в обработку исключений!!!
        data_for_save.to_sql(tabel_name, con=self.con, index=False)


    def giveValueOnTable(self, table_name: str) -> list:
        """
        На вход принимает имя таблицы
        Возвращает массив датафрейм со всеми данными 
        """
        sql = "SELECT * FROM " + table_name
        df = read_sql(sql=sql, con=self.con)
        return df.values