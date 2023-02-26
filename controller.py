from config import DATABASE_URI                 # параметры подключения к БД из модуля конфигурации config.py
from repository.connectorfactory import *       # подключаем фабрику коннекторов к БД
from repository.sql_api import *                # подключаем API для работы с БД

"""
    В данном модуле реализуются логика обработки клиентских запросов.
    Здесь также могут применяться SQL-методы, представленные в модуле repository.sql_api
"""

# Структура основного навигационнго меню веб-приложения,
# оформленное в виде массива dict объектов

# Получаем список обработанных файлов
def get_source_files_list():
    db_connector = SQLStoreConnectorFactory().get_connector(DATABASE_URI)  # получаем объект соединения
    result = select_all_from_source_files(db_connector)  # получаем список всех обработанных файлов
    # Завершаем работу с БД
    db_connector.close()
    return result

def get_source():
    db_connector = SQLStoreConnectorFactory().get_connector(DATABASE_URI)
    db_connector.start_transaction()
    qerry = f'SELECT id, first_name, last_name, country, city, email FROM Пользователь'
    results = db_connector.execute(qerry).fetchall()
    db_connector.end_transaction()
    return results