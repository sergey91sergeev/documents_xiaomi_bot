import sqlite3
import datetime
def create_table():
    """Функция создает базу данных bot.db и таблицы User и City"""
    connection = sqlite3.connect("bot.db")
    cursor = connection.cursor()
    try:
        cursor.execute('''BEGIN''')
        cursor.execute('''CREATE TABLE User (
        id_in_table_User INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        user_id INTEGER,
        user_name VARCHAR(50),
        user_surname VARCHAR(50),
        username VARCHAR(50),
        date_time DATETIME);''')

        cursor.execute('''CREATE TABLE Documents (
        id_in_table_City INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        user_id INTEGER,
        name_document VARCHAR(50),
        FOREIGN KEY (user_id) REFERENCES User(user_id));''')

        cursor.execute('''COMMIT''')
        print("Транзакция прошла успешно")

    except BaseException as e:
        cursor.execute('''ROLLBACK''')
        print(f"Ошибка в create_table: \n       {e} \nОткат транзакции")
    finally:
        connection.commit()
        cursor.close()
        connection.close()

# create_table()

def insert_into_table_User(user_id: int, user_name: str, user_surname: str, username: str, date_time: datetime):
    """Функция добавляет значения в таблицу User базы данных bot.db"""
    connection = sqlite3.connect("bot.db")
    cursor = connection.cursor()
    try:
        cursor.execute('''BEGIN''')
        cursor.execute('''INSERT INTO User (user_id, user_name, user_surname, username, date_time) VALUES (?, ?, ?, ?, ?);''',
                       (user_id, user_name, user_surname, username, date_time ))
        cursor.execute('''COMMIt''')
        print("Транзакция прошла успешно")
    except BaseException as e:
        cursor.execute('''ROLLBACK''')
        print(f"Ошибка в insert_into_table_User: \n       {e} \nОткат транзакции")
    finally:
        connection.commit()
        cursor.close()
        connection.close()

def insert_into_table_Documents(user_id: int, name_document: str):
    """Функция добавляет значения в таблицу City базы данных bot.db"""
    connection = sqlite3.connect("bot.db")
    cursor = connection.cursor()
    try:
        cursor.execute('''BEGIN''')
        cursor.execute('''INSERT INTO Documents(user_id, name_document) VALUES (?, ?);''',
                       (user_id, name_document))
        cursor.execute('''COMMIt''')
        print("Транзакция прошла успешно")
    except BaseException as e:
        cursor.execute('''ROLLBACK''')
        print(f"Ошибка в insert_into_table_Documents: \n       {e} \nОткат транзакции")
    finally:
        connection.commit()
        cursor.close()
        connection.close()




