import sqlite3

sql_students = '''
DROP TABLE IF EXISTS students;
CREATE TABLE students(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
fullname STRING,
group_id REFERENCES ggroups(id)
);
'''

sql_groups = '''
DROP TABLE IF EXISTS ggroups;
CREATE TABLE ggroups(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
name STRING
);
'''

sql_teachers = '''
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers(
id  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
fullname STRING
);
'''

sql_subjects = '''
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
name STRING,
teacher_id REFERENCES teachers(id)
);

'''

sql_grades = '''
DROP TABLE IF EXISTS grades;
CREATE TABLE grades(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    subject_id REFERENCES subjects(id),
    student_id REFERENCES students(id),
    grade INTEGER,
    date DATE
);
'''

def create():
    with sqlite3.connect("college.db") as connect:
        cursor = connect.cursor()
        cursor.executescript(sql_students)
        cursor.executescript(sql_groups)
        cursor.executescript(sql_subjects)
        cursor.executescript(sql_teachers)
        cursor.executescript(sql_grades)
        cursor.close()

    connect.close()



create()