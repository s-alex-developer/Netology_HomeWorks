from models import Publisher, Book, Shop, Stock, Sale


def add_publisher(session, func_arg: dict):

    """
        1. Функция добавляет строку данных в таблицу Publisher
        2. Первым аргументом функция принимает объект sesssion класса Session
        3. Вторым аргументом функция принимает словарь содержащий данные для добавления в БД
    """

    session.add(Publisher(name=func_arg["name"]))
    session.commit()


def add_book(session, func_arg: dict):

    """
        1. Функция добавляет строку данных в таблицу Book
        2. Первым аргументом функция принимает объект sesssion класса Session
        3. Вторым аргументом функция принимает словарь содержащий данные для добавления в БД
    """

    session.add(Book(title=func_arg["title"], id_publisher=func_arg["id_publisher"]))
    session.commit()


def add_shop(session, func_arg: dict):

    """
        1. Функция добавляет строку данных в таблицу Shop
        2. Первым аргументом функция принимает объект sesssion класса Session
        3. Вторым аргументом функция принимает словарь содержащий данные для добавления в БД
    """

    session.add(Shop(name=func_arg["name"]))
    session.commit()


def add_stock(session, func_arg: dict):

    """
        1. Функция добавляет строку данных в таблицу Stock
        2. Первым аргументом функция принимает объект sesssion класса Session
        3. Вторым аргументом функция принимает словарь содержащий данные для добавления в БД
    """

    session.add(Stock(id_shop=func_arg["id_shop"], id_book=func_arg["id_book"],
                      count=func_arg["count"]))
    session.commit()


def add_sale(session, func_arg: dict):

    """
        1. Функция добавляет строку данных в таблицу Sale
        2. Первым аргументом функция принимает объект sesssion класса Session
        3. Вторым аргументом функция принимает словарь содержащий данные для добавления в БД
    """

    session.add(Sale(price=func_arg["price"], date_sale=func_arg["date_sale"],
                     count=func_arg["count"], id_stock=func_arg["id_stock"]))
    session.commit()