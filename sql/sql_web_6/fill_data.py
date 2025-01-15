from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_CLASSES = 3
NUMBER_STUDENTS = 30
NUMBER_GROUPS = 3
NUMBER_TEACHERS = 5
fake_data = faker.Faker('uk_UA')


def generate_fake_data( number_students, number_teachers) -> tuple():
    fake_groups = ['UA1', 'ENG2', 'PL3']  # тут зберігатимемо компанії
    fake_students = []  # тут зберігатимемо співробітників
    fake_classes = ["Math", "Physics", "Philosophy", "History", "Ukrainian language"]
    fake_teachers = []
    # тут зберігатимемо посади
    '''Візьмемо три компанії з faker і помістимо їх у потрібну змінну'''


    # Створимо набір компаній у кількості number_companies
    for _ in range(number_students):
        fake_students.append(fake_data.name())
    # Згенеруємо тепер number_employees кількість співробітників'''
    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    return fake_classes, fake_students,fake_groups, fake_teachers


def prepare_data(classes, students, groups, teachers) -> tuple():
    for_groups = []
    # підготовляємо список кортежів назв компаній
    for gr in groups:
        for_groups.append((gr, ))

    for_students = []  # для таблиці employees

    for student in students:
        '''
        Для записів у таблицю співробітників нам треба додати посаду та id компанії. Компаній у нас було за замовчуванням
        NUMBER_COMPANIES, при створенні таблиці companies для поля id ми вказували INTEGER AUTOINCREMENT - тому кожен
        запис отримуватиме послідовне число збільшене на 1, починаючи з 1. Тому компанію вибираємо випадково
        у цьому діапазоні
        '''
        for_students.append((student, randint(1, NUMBER_GROUPS)))

    '''
    Подібні операції виконаємо й у таблиці payments виплати зарплат. Приймемо, що виплата зарплати у всіх компаніях
    виконувалася з 10 по 20 числа кожного місяця. Вилку зарплат генеруватимемо в діапазоні від 1000 до 10000 у.о.
    для кожного місяця, та кожного співробітника.
    '''
    for_teachers = []

    for couch in teachers:
        # Виконуємо цикл по місяцях'''
        # payment_date = datetime(2021, month, randint(10, 20)).date()

        for_teachers.append((couch, ))

    for_classes = []  # для таблиці employees

    for cl in classes:

        for_classes.append((cl, randint(1, NUMBER_TEACHERS)))

    for_marks = []

    for _ in range(1, 150):

        fake_date = fake_data.date()
        for_marks.append((randint(5, 12), fake_date, randint(1, NUMBER_CLASSES), randint(1, NUMBER_STUDENTS)))


    return for_groups, for_students, for_teachers, for_classes, for_marks



def insert_data_to_db(groups, students, teachers, classes, marks) -> None:
    # Створимо з'єднання з нашою БД та отримаємо об'єкт курсору для маніпуляцій з даними

    with sqlite3.connect('tables.db') as con:

        cur = con.cursor()

        '''Заповнюємо таблицю компаній. І створюємо скрипт для вставки, де змінні, які вставлятимемо відзначимо
        знаком заповнювача (?) '''

        sql_to_groups = """INSERT INTO groups(group_name)
                               VALUES (?)"""

        '''Для вставки відразу всіх даних скористаємося методом executemany курсора. Першим параметром буде текст
        скрипта, а другим дані (список кортежів).'''

        cur.executemany(sql_to_groups, groups)

        # Далі вставляємо дані про співробітників. Напишемо для нього скрипт і вкажемо змінні

        sql_to_students = """INSERT INTO students(fullname, group_id)
                               VALUES (?, ?)"""

        # Дані були підготовлені заздалегідь, тому просто передаємо їх у функцію

        cur.executemany(sql_to_students, students)

        # Останньою заповнюємо таблицю із зарплатами

        sql_to_teachers = """INSERT INTO teachers(fullname)
                              VALUES (?)"""

        # Вставляємо дані про зарплати

        cur.executemany(sql_to_teachers, teachers)



        # Останньою заповнюємо таблицю із зарплатами

        sql_to_classes = """INSERT INTO classes(class_name, teacher_id)
                                      VALUES (?, ?)"""

        # Вставляємо дані про зарплати

        cur.executemany(sql_to_classes, classes)

        sql_to_marks = """INSERT INTO marks(mark, date_of, class_id, student_id)
                                               VALUES (?, ?, ?, ?)"""

        # Дані були підготовлені заздалегідь, тому просто передаємо їх у функцію

        cur.executemany(sql_to_marks, marks)


        # Фіксуємо наші зміни в БД

        con.commit()

if __name__ == "__main__":
    groups, students, teachers, classes, marks = prepare_data(*generate_fake_data(NUMBER_STUDENTS, NUMBER_TEACHERS))
    insert_data_to_db(groups, students, teachers, classes, marks)