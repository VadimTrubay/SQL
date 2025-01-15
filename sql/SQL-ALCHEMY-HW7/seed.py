from datetime import date, datetime, timedelta
from pprint import pprint
from random import choice, randint

import faker

from models import *

fake = faker.Faker()

STUDENTS = 50
TEACHERS = 5
GROUPS = ["СБУ-14","ПГС-13","АРХ-12"]
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
    "French Language"
    ]


def seed_students():
    adding = []
    for i in range(1,STUDENTS+1):
        adding.append((Students(name = fake.name(), group_id = randint(1,len(GROUPS)))))
    session.add_all(adding)
    session.commit()

def seed_groups():
    groups = []

    for i in GROUPS:
        groups.append((Groups(name = i)))

    session.add_all(groups)
    session.commit()

def seed_teachers():
    teachers = []
    for i in range(0,TEACHERS):
        teachers.append(
            Teachers(name = fake.name())
            )
    session.add_all(teachers)
    session.commit()
    
def seed_subjects():
    subjects = []

    for i in SUBJECTS:
        subjects.append(Subjects(name = i, teacher_id = randint(1,TEACHERS)))
    
    session.add_all(subjects)
    session.commit()

def seed_grades():
    grades =[]
    dates = generate_dates()

    for date in dates:
        rand_subj = randint(1,len(SUBJECTS))
        rand_stud = [randint(1,STUDENTS) for i in range(5)]
        for student in rand_stud:
            grades.append((Grades(subject_id = rand_subj,
                                  student_id = student,
                                  grade = randint(1,12),
                                  date = date)))

    session.add_all(grades)
    session.commit()
    return grades            
    
def generate_dates():
    dates = []
    start =datetime.strptime("2023-01-01","%Y-%d-%m").date()
    end = datetime.strptime("2023-10-01", "%Y-%m-%d").date()
    delta = timedelta(days=1)
    while start < end:
        dates.append(start)
        start = start+delta
    
    return dates

if __name__ == "__main__":
    seed_students()
    seed_groups()
    seed_subjects()
    seed_teachers()
    seed_grades()