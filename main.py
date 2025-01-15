import sqlite3


def main():
    create_db()


def create_db():
    SQL_DB = "SQL_DB.sql"
    DB = "DB.db"

    # читаємо файл зі скриптом для створення БД
    with open(SQL_DB) as f:
        sql = f.read()

    # створюємо з'єднання з БД (якщо файлу з БД немає, він буде створений)
    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()
        # виконуємо скрипт із файлу, який створить таблиці в БД
        cur.executescript(sql)


if __name__ == "__main__":
    main()
