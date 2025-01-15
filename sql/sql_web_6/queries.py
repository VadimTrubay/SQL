import sqlite3

"""Найти 5 студентов с наибольшим средним баллом по всем предметам."""

def execute_query(sql: str) -> list:
    with sqlite3.connect('tables.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql_1 = """
SELECT s.fullname, ROUND(AVG(m.mark), 2) as result_mark
FROM marks m
LEFT JOIN students s ON s.id = m.student_id
GROUP BY s.fullname
ORDER BY result_mark DESC
LIMIT 5;
"""

"""Найти студента с наивысшим средним баллом по определенному предмету."""

sql_2 = """
SELECT c.class_name, s.fullname, ROUND(AVG(m.mark), 2) as result_mark
FROM marks m
JOIN students s ON s.id = m.student_id
JOIN classes c ON c.id = m.class_id
WHERE c.id = 1
GROUP BY s.fullname
ORDER BY result_mark DESC
LIMIT 1;
"""

"""Найти средний балл в группах по определенному предмету."""

sql_3 = """
SELECT g.group_name, c.class_name, ROUND(AVG(m.mark), 2) as result_mark
FROM marks m, groups g
JOIN students s ON g.id = m.student_id
JOIN classes c ON c.id = m.class_id
WHERE c.id = 1
GROUP BY g.group_name
ORDER BY result_mark DESC
LIMIT 1;
"""

"""Найти средний балл на потоке (по всей таблице оценок)"""

sql_4 = """
SELECT ROUND(AVG(m.mark), 2) as result_mark
FROM marks m
LIMIT 1;
"""

"""Найти какие курсы читает определенный преподаватель."""
sql_5 = """
SELECT t.fullname, c.class_name as result
FROM classes c
JOIN teachers t ON t.id = c.teacher_id
WHERE t.id = 1
"""

"""Найти список студентов в определенной группе."""
sql_6 = """
SELECT s.fullname, g.group_name as result
FROM groups g
JOIN students s ON g.id = s.group_id
WHERE g.id = 3
"""
"""Найти оценки студентов в отдельной группе по определенному предмету."""
sql_7 = """
SELECT m.mark, s.fullname, g.group_name, c.class_name
FROM marks m
JOIN students s ON s.id = m.student_id
JOIN groups g ON g.id = s.group_id
JOIN classes c ON c.id = m.class_id
WHERE g.id = 3 AND c.id = 3
"""
"""Найти средний балл, который ставит определенный 
преподаватель по своим предметам."""
sql_8 = """
SELECT t.fullname, ROUND(AVG(m.mark), 2)
FROM marks m
JOIN classes c ON c.id = m.class_id
JOIN teachers t ON t.id = c.teacher_id
WHERE t.id = 1
GROUP BY c.class_name
"""

"""список курсов, которые посещает определенный студент."""
sql_9 = """
SELECT s.fullname, c.class_name
FROM marks m
JOIN classes c ON c.id = m.class_id
JOIN students s ON s.id = m.student_id
WHERE s.id = 1
GROUP BY c.class_name
"""

"""Список курсов, которые определенному студенту читает определенный преподаватель."""

sql_10 = """
SELECT c.class_name
FROM marks m
JOIN teachers t ON t.id = c.teacher_id
JOIN students s ON s.id = m.student_id
JOIN classes c ON c.id = m.class_id
WHERE s.id = 1 AND t.id = 4
"""

"""Средний балл, который определенный преподаватель ставит определенному студенту."""

sql_11 = """
SELECT t.fullname, s.fullname, c.class_name, ROUND(AVG(m.mark), 2) 
FROM marks m
JOIN teachers t ON t.id = c.teacher_id
JOIN students s ON s.id = m.student_id
JOIN classes c ON c.id = m.class_id
WHERE t.id = 1 AND s.id = 4
"""

queries_dict = {1:sql_1, 2:sql_2, 3:sql_3, 4:sql_4, 5:sql_5, 6:sql_6, 7:sql_7, 8:sql_8, 9:sql_9, 10:sql_10, 11:sql_11}


if __name__ =="__main__":
    while True:
        user_input = input('Choose SQL query: ')
        if user_input == 'exit':
            break
        else:
            try:
                print(execute_query(queries_dict.get(int(user_input))))
            except ValueError as err:
                print(f"Incorrect input: {user_input}!!!, Please use integers from 1 to 10")
