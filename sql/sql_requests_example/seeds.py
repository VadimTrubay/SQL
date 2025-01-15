import sqlite3
from datetime import datetime, timedelta
from random import randint

import faker

fake = faker.Faker()

BASE = "college.db"
STUDENTS = 50
TEACHERS = 5
GROUPS = ["СБУ-14", "ПГС-13", "АРХ-12"]
SUBJECTS = [
    "English Language",
    "Mathematic",
    "History",
    "Programming",
    "Biology",
    "Physics",
    "Chemistry",
    "Astronomy",
    "Ukrainian Language",
    "Design",
    "Spain Language",
    "Geography",
    "Geometry",
    "French Language",
]


def seed_students():
    students_prepare = [fake.name() for i in range(STUDENTS)]
    groups = [randint(1, 3) for i in range(0, STUDENTS)]
    students_to_sql = zip(students_prepare, groups)

    sqlScript = """
    INSERT INTO students(fullname, group_id)
    VALUES(?,?);
    """
    with sqlite3.connect(BASE) as connect:
        cursor = connect.cursor()
        cursor.executemany(sqlScript, students_to_sql)

        cursor.close()
    connect.close()


def seed_groups():
    sqlScript = """
    INSERT INTO ggroups(name)
    VALUES(?)
    """
    with sqlite3.connect(BASE) as connect:
        cursor = connect.cursor()
        for i in GROUPS:
            cursor.execute(sqlScript, (i,))

        cursor.close()
    connect.close()


def seed_teachers():
    sqlScript = """
    INSERT INTO teachers(fullname)
    VALUES(?);
    """
    teachers = [fake.name() for i in range(TEACHERS)]
    with sqlite3.connect(BASE) as connect:
        cursor = connect.cursor()
        for i in teachers:
            cursor.execute(sqlScript, (i,))
        cursor.close()
    connect.close()


def seed_subjects():
    sqlScript = """
    INSERT INTO subjects(name, teacher_id)
    VALUES (?,?);
    """
    teachers = [(i, randint(1, TEACHERS)) for i in SUBJECTS]
    with sqlite3.connect(BASE) as connect:
        cursor = connect.cursor()
        cursor.executemany(sqlScript, teachers)
        cursor.close()

    connect.close()


def list_dates():
    dates = []
    start = datetime.strptime("2023.01.01", "%Y.%m.%d").date()
    end = datetime.strptime("2023.12.25", "%Y.%m.%d").date()
    plusDay = timedelta(days=1)
    grade_date = start
    while grade_date < end:
        grade_date: datetime

        if grade_date.isoweekday() <= 5:
            dates.append(grade_date)
        grade_date += plusDay

    return dates


def seed_grades():
    grades = []
    days = list_dates()

    for day in days:
        rand_subject = randint(1, len(SUBJECTS))
        rand_students = [randint(1, STUDENTS) for i in range(5)]
        for student in rand_students:
            grades.append((rand_subject, student, randint(1, 12), day))

    sqlScript = """
    INSERT INTO grades(subject_id, student_id, grade, date)
    VALUES (?,?,?,?)
    """

    with sqlite3.connect(BASE) as connect:
        cursor = connect.cursor()
        cursor.executemany(sqlScript, grades)

    return grades


if __name__ == "__main__":
    seed_students()
    seed_groups()
    seed_teachers()
    seed_subjects()
    seed_grades()
