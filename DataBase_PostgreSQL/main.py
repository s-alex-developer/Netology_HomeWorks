import psycopg2
from pprint import pprint


class DataBase:
    pass

    def __init__(self, _db_name, _db_user, _user_password):
        self.name = _db_name
        self.user = _db_user
        self.password = _user_password

# ДОПОЛНИТЕЛЬНЫЕ И ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ.

    def __with(self, *args):

        """
            Функция открывает/закрывает соединение с БД (ничего не возвращает).
            В качестве аргумента принимает SQL запрос.
        """

        with psycopg2.connect(database=self.name, user=self.user, password=self.password) as conn:
            with conn.cursor() as cur:
                cur.execute(*args)

    def __with_fetchone(self, *args):

        """
            Функция открывает/закрывает соединение с БД (возвращает одну строку).
            В качестве аргумента принимает SQL запрос.
        """

        with psycopg2.connect(database=self.name, user=self.user, password=self.password) as conn:
            with conn.cursor() as cur:
                cur.execute(*args)
                return cur.fetchone()

    def __with_fetchall(self, *args):

        """
            Функция открывает/закрывает соединение с БД (возвращает все строки).
            В качестве аргумента принимает SQL запрос.
        """

        with psycopg2.connect(database=self.name, user=self.user, password=self.password) as conn:
            with conn.cursor() as cur:
                cur.execute(*args)
                return cur.fetchall()

    def __get_id_from_email(self, email: str):

        """ Функция принимает email клиента и возвращает id этого клиента из таблицы clients. """

        select_request = \
            """
                SELECT *
                FROM clients
                WHERE email = %s;
            """
        id = str((self.__with_fetchone(select_request, [email]))[0])
        return id

    def __get_id_from_phone(self, phone_number: str):

        """Функция принимает номер телефона клиента и возвращает id этого клиента из таблицы phone_numbers. """

        select_request = \
            """
                SELECT *
                FROM phone_numbers
                WHERE phone_number = %s;
            """
        id = str((self.__with_fetchone(select_request, [phone_number]))[2])
        return id

    def delete_table(self):

        """ Функция каскадного удаления таблиц clients и phone_numbers из БД. """

        delete_request = \
            """
                DROP TABLE clients, 
                           phone_numbers;
            """
        self.__with(delete_request)

    def client_info(self, id: str = None, email: str = None):

        """
            1. Функция выводит сводную информацию о клиенте из таблиц clients и phone_numbers
            2. Поиск клиента осуществляется по полям id или email в таблице clients
            3. Для выполнения поиска достаточно передать один аргумента на выбор
            4. Приоритет аргументов при выполнении поиска: id, email
            5. Порядков вывода полей:
                - из таблицы clients: id, first_name, last_name, email
                - из таблицы phone_numbers: id, phone_number
            6. Если пользователь указал 2 телефонных номера и более, мы получим несколько записей
        """

        if id is None:
            id = self.__get_id_from_email(email)

        select_request = \
            """
                SELECT cl.id,
                       cl.first_name,
                       cl.last_name,
                       cl.email,
                       pn.id,
                       pn.phone_number
                  FROM clients AS cl
                       LEFT JOIN phone_numbers AS pn
                              ON pn.client_id = cl.id
                 WHERE cl.id = %s;
            """
        resp = self.__with_fetchall(select_request, id)
        return resp

# ФУНКЦИИ ИЗ ДОМАШНЕГО ЗАДАНИЯ.

    # ЗАДАНИЕ 1. Функция, создающая структуру БД (таблицы clients и phone_numbers).

    def create_table(self):

        """ Функция создает структуру таблиц clients и phone_numbers"""

        create_request = \
            """
                CREATE TABLE IF NOT EXISTS clients (
                     PRIMARY KEY (id),
                          id SERIAL,
                  first_name VARCHAR(50) NOT NULL 
                             CHECK (first_name != ''),
                   last_name VARCHAR(50) NOT NULL 
                             CHECK (last_name != ''),
                       email VARCHAR(50) NOT NULL 
                             UNIQUE 
                             CHECK (email != '')
               );

               CREATE TABLE IF NOT EXISTS phone_numbers (
                    PRIMARY KEY (id),
                         id SERIAL,
               phone_number VARCHAR(50) NOT NULL 
                            UNIQUE
                            CHECK (phone_number != ''),
                  client_id INTEGER NOT NULL,
                            FOREIGN KEY (client_id) REFERENCES  clients(id) 
                            ON DELETE CASCADE,
                            UNIQUE (client_id, phone_number)
               );

            """
        self.__with(create_request)

    # ЗАДАНИЕ 2. Функция, позволяющая добавить нового клиента.

    def insert_client(
            self,
            id: str,
            first_name: str,
            last_name: str,
            email: str
    ):

        """
            1. Функция добавляет нового клиента в таблицу clients
            2. Может принимать 4 именованных аргумента: id=, first_name=, last_name=, email=
            3. Имена аргументов идентичны именам полей в таблице clients
            4. Значения аргументов должны содержать только строковые данные, но не могут быть пустрой строкой
            5. Для работы функции необходимо передать ВСЕ 4 АРГУМЕНТА!!!

        """

        insert_request = \
            """
                INSERT INTO clients (id, first_name, last_name, email)
                VALUES (%s, %s, %s, %s);
            """

        self.__with(insert_request, [id, first_name, last_name, email])

    # ЗАДАНИЕ 3. Функция, позволяющая добавить телефон для существующего клиента.

    def insert_phone_number(
            self,
            phone_number: str = None,
            client_id: str = None,
            email: str = None
    ):

        """
            1. Функция добавляет номер телефона в таблицу phone_numbers для существующего клиента из таблицы clients
            2. Может принимать до 3 именованных аргументов: id=, email=, phone_number=
            2. Имена аргументов идентичны именам полей в таблице clients и phone_numbers
            3. Идентификация клиента осуществляется по полям id или email в таблице clients
            4. Для выполнения идентификации достаточно передать один аргумента на выбор
            5. Приоритет аргументов при выполнении идентификации клиента: id, email
            6. Передача аргумента phone_number= является обязательной
            7. Значения аргументов должны содержать только строковые данные, но не могут быть пустрой строкой

        """

        if client_id is None and email is not None:
            client_id = self.__get_id_from_email(email)

        insert_request = \
            """
            INSERT INTO phone_numbers (phone_number, client_id)
            VALUES (%s, %s);
            """
        self.__with(insert_request, [phone_number, client_id])

    # ЗАДАНИЕ 4. Функция, позволяющая изменить данные о клиенте.

    def update_client(self, id: str = None, email: str = None, **kwargs):

        """
            1. Функция позволяет изменять данные клиента в таблицах clients и phone_numbers.
            2. Может принимать до 2-х обязательных именованных аргументов: id=, email=
            3. Может принимать до 4-х именованных аргументов содержащих данные для обновления информации о клиенте.
            4. Идентификация клиента осуществляется по полям id или email в таблице clients
            5. Для выполнения идентификации достаточно передать один аргумента на выбор
            6. Приоритет аргументов при выполнении идентификации клиента: id, email
            7. Имена аргументов без префикса new_ идентичны именам полей в таблице clients и phone_numbers,
            8. Префикс new_ имеют имена аргументов содержащие данные для обновления
                 new_first_name=
                 new_last_name=
                 new_email=
                 new_phone_number=
            9. Для работы функции необходимо передать хотя бы по 1 аргументу идентификации клиента и обновления данных.
            10. Если пользователь указал 2 телефонных номера и более, то в диалоговом окне будет предоставлена
                возможность выбора номера для изменения.

        """

        if id is None:
            id = self.__get_id_from_email(email)

        for k, v in kwargs.items():

            if k[4:] != 'phone_number':

                update_request = """ UPDATE clients \
                    SET {}='{}' WHERE id = {}""".format(k[4:], v, id)

                self.__with(update_request)

            elif k[4:] == 'phone_number':

                info = self.client_info(id)

                count = len(self.client_info(id))

                if count > 1:

                    print(f'\nКол-во телефонных номеров у пользователя c id {id}: {count} номера.\n')

                    pprint(info)

                    id = input(f"\nВведите id телефонного номера (цифра перед номером)"
                                     f",который хотите изменить: ")

                    update_request = """ UPDATE phone_numbers \
                                            SET {}='{}' WHERE id = {}""".format(k[4:], v, id)

                    self.__with(update_request)

                else:
                    update_request = """ UPDATE phone_numbers \
                        SET {}='{}' WHERE client_id = {}""".format(k[4:], v, id)

                    self.__with(update_request)

    # ЗАДАНИЕ 5. Функция, позволяющая удалить телефон для существующего клиента.

    def delete_phone(self, id: str = None, email: str = None, phone_number: str = None):

        """
            1. Функция позволяет удалить телефон для существующего клиента из таблицы phone_numbers
            2. Может принимать до 3-х именованных аргументов: id=, email=, phone_number
            3. Поиск записи для удаления номера телефона может осуществлятся по любому из передаваемых аргументов
            4. Для выполнения удаления достаточно передать один аргумент на выбор
            6. Приоритет аргументов при выполнении поиска: id, email, phone_number
            7. Если за пользователем закреплено 2 телефонных номера и более, а поиск производится по полям id или email,
                то в диалоговом окне будет предоставлена возможность выбора номера для удаления
            8. Применение аргумента phone_number сразу удаляет запись из таблицы phone_numbers

        """

        if id is None and email is not None:
            id = self.__get_id_from_email(email)

        elif id is None and phone_number is not None:
            id = self.__get_id_from_phone(phone_number)

        info = self.client_info(id)

        count = len(self.client_info(id))

        if count > 1:

            print(f'\nКол-во телефонных номеров у пользователя c id {id}: {count} номера.\n')

            pprint(info)

            phone_id = input(f"\nВведите phone_id телефонного номера (цифра перед номером)"
                             f",который хотите удалить: ")

            delete_request = """ DELETE FROM phone_numbers WHERE id = %s"""

            self.__with(delete_request, phone_id)

        else:
            delete_request = """ DELETE FROM phone_numbers WHERE client_id = %s"""
            self.__with(delete_request, id)

    # ЗАДАНИЕ 6. Функция, позволяющая удалить существующего клиента.

    def delete_client(self, id: str = None, email: str = None):

        """
            1. Функция позволяет удалить существующего клиента и всю связанную с ним информацию из таблиц clients и
               phone_numbers.
            2. Может принимать до 2-х именованных аргументов: id=, email=
            3. Поиск записи для удаления может осуществлятся по любому из передаваемых аргументов
            4. Для выполнения удаления достаточно передать один аргумент на выбор
            5. Приоритет аргументов при выполнении поиска: id, email
        """

        if id is None:
            id = self.__get_id_from_email(email)

        delete_request = \
            """
                DELETE FROM clients WHERE id = %s
            """
        self.__with(delete_request, id)

    # ЗАДАНИЕ 7. Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону.

    def find_client(self, **kwargs):

        """
            1. Функция производит поиск клиента по указанные данным в таблицах client и phone_numbers
            2. Может принимать до 4-х именованных аргументов: first_name=, last_name=, email=', phone_number=
            3. Поиск клиента может осуществлятся по любому из передаваемых аргументов
            4. Для выполнения поиска достаточно передать один аргумент на выбор,
               но каждый следующий переданный аргумент увеличивает валидацию полученных данных.
        """

        where_requests = ''
        limit = len(kwargs)
        count = 0

        for k, v in kwargs.items():
            count += 1
            if k != 'phone_number':
                where_requests += " cl.{} = '{}'".format(k, v)
            else:
                where_requests += " pn.{} = '{}'".format(k, v)

            if count < limit:
                where_requests += ' AND'
            else:
                where_requests += ';'

        select_request = \
            """
            SELECT cl.id,
                   cl.first_name,
                   cl.last_name,
                   cl.email,
                   pn.id,
                   pn.phone_number
            FROM clients AS cl
            LEFT JOIN phone_numbers AS pn
                 ON pn.client_id = cl.id
            WHERE
            """

        select_request += where_requests
        response = self.__with_fetchall(select_request)
        pprint(response)
        print()


if __name__ == '__main__':

    # ПАРАМЕТРЫ ПОДКЛЮЧЕНИЯ К БД:

    db_name: str = ''
    db_user: str = ''
    user_password: str = ''

    test_db = DataBase(db_name, db_user, user_password)

    # 0. УДАЛЕНИЕ ТАБЛИЦ:

    test_db.delete_table()

    # 1. СОЗДАНИЕ ТАБЛИЦ:

    test_db.create_table()

    # 2. ДОБАВЛЕНИЕ КЛИЕНТОВ:

    test_db.insert_client(id='1', first_name='Joey', last_name='Jordison', email='j.jordison@gmail.com')
    test_db.insert_client(id='2', first_name='Lars', last_name='Ulrich', email='l.urlich@gmail.com')
    test_db.insert_client(id='3', first_name='Nicko', last_name='McBrain', email='n.mcbrain@gmail.com')
    test_db.insert_client(id='4', first_name='Travis', last_name='Barker', email='t.barker@gmail.com')
    test_db.insert_client(id='5', first_name='Dave', last_name='Lombardo', email='d.lombardo@gmail.com')
    test_db.insert_client(id='6', first_name='Dave', last_name='Weckl', email='d.weckl@gmail.com')

    # 3. ДОБАВЛЕНИЕ НОМЕРОВ ТЕЛЕФОНА СУЩЕСТВУЮЩИМ КЛИЕНТАМ:

    # Номер телефона для клиента с id=1 не указан.
    test_db.insert_phone_number(phone_number='+7 (777) 2222222', client_id='2')
    test_db.insert_phone_number(phone_number='+7 (777) 3333333', client_id='3')
    test_db.insert_phone_number(phone_number='+7 (777) 4444444', client_id='4')
    test_db.insert_phone_number(phone_number='+7 (777) 5555555', client_id='5')
    test_db.insert_phone_number(phone_number='+7 (999) 5555555', email='d.lombardo@gmail.com')
    test_db.insert_phone_number(phone_number='+7 (777) 6666666', client_id='6')
    test_db.insert_phone_number(phone_number='+7 (999) 6666666', client_id='6', email='d.weckl@gmail.com')

    # 4. ИЗМЕНЕНИЕ ДАННЫХ О КЛИЕТАХ:

    # >>> Готовые варианты запросов для проверки:

    # test_db.update_client(id='1', new_first_name='new_name')
    # test_db.update_client(id='2', new_first_name='new_name', new_last_name='new_last_name')
    # test_db.update_client(id='3', new_first_name='new_name', new_last_name='new_last_name', new_email='new_email_1')
    #
    # test_db.update_client(id='4', new_first_name='new_name', new_last_name='new_last_name',
    #                       new_email='new_email_2', new_phone_number='new_number_2')
    #
    # test_db.update_client(id='5', new_first_name='new_name', new_last_name='new_last_name',
    #                       new_email='new_email_3', new_phone_number='new_number_3')
    #
    # test_db.update_client(email='d.weckl@gmail.com', new_email='new_email_4', new_phone_number='new_number_4')

    # 5. УДАЛЕНИЕ НОМЕРОВ ТЕЛЕФОНОВ У СУЩЕСТВУЮЩИХ КЛИЕНТОВ:

    # >>> Готовые варианты запросов для проверки:

    # test_db.delete_phone(id='1')
    # test_db.delete_phone(email='l.urlich@gmail.com')
    # test_db.delete_phone(phone_number='+7 (777) 3333333')
    # test_db.delete_phone(id='5')

    # 6 УДАЛЕНИЕ КЛИЕНТОВ:

    # >>> Готовые варианты запросов для проверки:

    # test_db.delete_client(id='4')
    # test_db.delete_client(email='d.lombardo@gmail.com')
    # test_db.delete_client(email='l.urlich@gmail.com', id='6')  # Передан заведомо неверный email

    # 7 ПОИСК КЛИЕНТОВ:

    # >>> Готовые варианты запросов для проверки:

    # test_db.find_client(first_name='Joey')  # Номер телефона данного клиента не указан.
    # test_db.find_client(last_name='Ulrich')
    # test_db.find_client(email='n.mcbrain@gmail.com')
    # test_db.find_client(phone_number='+7 (777) 4444444')
    # test_db.find_client(first_name='Dave')
    # test_db.find_client(first_name='Dave', last_name='Lombardo')
    # test_db.find_client(first_name='Dave', email='d.weckl@gmail.com')
    # test_db.find_client(first_name='Dave', phone_number='+7 (999) 6666666')

#                          >>> *** THE END *** <<<

