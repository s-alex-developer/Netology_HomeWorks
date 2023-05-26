import os
import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, find_dotenv

from func_add_rows import *
from models import create_tables, delete_tables

""" 
    ЗАДАНИЕ 2. Напишите Python-скрипт, который:
        1. Подключается к БД любого типа на ваш выбор, например, к PostgreSQL;
        2. Импортирует необходимые модели данных;
        3. Принимает имя или идентификатор издателя (publisher), например, через input(). 
        4. Выводит построчно факты покупки книг этого издателя:
"""


''' Для работы скрипта необходимо добавить значения переменных окружения в файл .env '''

if __name__ == '__main__':

    # Поиск и загрузка файла с переменными окружения в каталоге проекта:

    load_dotenv(find_dotenv())

    # Формируем строку запроса для подключения к нашей БД:

    DNS = f"postgresql://{os.getenv('user')}:{os.getenv('password')}" \
          f"@{os.getenv('host_name')}:{os.getenv('port')}/{os.getenv('db_name')}"

    # Создаем движок:

    engine = sqlalchemy.create_engine(DNS)

    # Создание базового класса:

    Session = sessionmaker(bind=engine)

    # Инициализируем экеземпляр класса Session, умеющий создавать сессии подключения к БД:

    session = Session()

    # Метод удаление таблиц из БД:

    delete_tables(engine)

    # Метод создания таблиц в БД:

    create_tables(engine)

    """ 
        ЗАДАНИЕ 3 (необезательное). 
            1. Заполните БД тестовыми данными. 
    """

    with open(os.getenv("data_file")) as f:

        for el in json.load(f):

            work_dict = el["fields"]

            """
                1. Определение таблицы для добавления данные происходит по значению ключа 'model'
                2. Массив данных (словарь) для добавления в БД доступен по ключу "fields".
            """

            if el['model'] == "publisher":
                add_publisher(session, work_dict)

            if el['model'] == "book":
                add_book(session, work_dict)

            if el['model'] == "shop":
                add_shop(session, work_dict)

            if el['model'] == "stock":
                add_stock(session, work_dict)

            if el['model'] == "sale":
                add_sale(session, work_dict)

    """ РАБОТА C БД (ПРОДОЛЖЕНИЕ ЗАДАНИЯ 2). """

    publisher_id = input('Введите id или имя автора: ').strip("\"' ")

    if publisher_id.isdigit() is not True:

        query = session.query(Publisher.id).filter(Publisher.name == publisher_id)

        for c in query:
            publisher_id = c.id

    query = session.query(Book.title, Shop.name, Sale.price * Sale.count, Sale.date_sale) \
        .join(Publisher).join(Stock).join(Shop).join(Sale).filter(Publisher.id == publisher_id)

    template = ' {: <40} | {: <10} | {: <8} | {} |'

    for c in query:
        print(template.format(c[0], c[1], c[2], c[3].date()))

    # Закрытие сессии работы с БД:

    session.close()
