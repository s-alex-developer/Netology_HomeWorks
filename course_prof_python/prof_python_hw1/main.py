import os
from datetime import datetime
from dotenv import find_dotenv, load_dotenv

from application.salary import calculate_salary
from application.db.people import get_employees


if __name__ == '__main__':

    date = datetime.today().date()
    load_dotenv(find_dotenv())

    print(f'\n{os.getenv("guest_name")} Сегодняшняя дата: {date}.\n')

    calculate_salary()

    get_employees()