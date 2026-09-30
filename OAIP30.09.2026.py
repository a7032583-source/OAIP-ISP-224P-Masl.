import sqlite3
import os

DB_NAME = 'students.db'

def main():
    db_exists = os.path.exists(DB_NAME)
    conn = create_connection()
    if not db_exists:
        create_table(conn)
        add_sample_data(conn)
    view_data(conn)
    while True:
        print("\n===== УЧЁТ СТУДЕНТОВ =====")
        print("1. Показать всех студентов")
        print("2. Добавить студента")
        print("3. Найти студентов по группе")
        print("4. Найти студентов по оценке")
        print("5. Изменить оценку")
        print("6. Удалить студента")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == '0':
            print("Выход из программы.")
            conn.close()
            break
        elif choice == '1':
            view_data(conn)
        elif choice == '2':
            add_student_data(conn)
        elif choice == '3':
            search_by_group(conn)
        elif choice == '4':
            search_by_grade(conn)
        elif choice == '5':
            update_grade(conn)
        elif choice == '6':
            delete_student(conn)
        else:
            print("Неверный ввод. Пожалуйста, выберите число от 0 до 7.")

def create_connection():
    conn = sqlite3.connect('students.db')
    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE students (
    id integer PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    group_name TEXT NOT NULL,
    grade INTEGER NOT NULL)''')
    conn.commit()

def add_sample_data(conn):
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO students (name, group_name, grade) VALUES
    ('Иванов Иван', 'ИСП-324П', 5),
    ('Петров Пётр', 'ИСП-225П', 4),
    ('Сидоров Сидр', 'ИСП-324П', 3),
    ('Анненкова Анна', 'ИСП-126П', 5),
    ('Кузнецов Кузнечик', 'ИСП-126П', 4)''')

def view_data(conn):
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM students''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def add_student_data(conn):
    name = input("Введите имя студента: ")
    group = input("Введите имя группы: ")
    grade = int(input("Введите оценку студента: "))
    while grade < 2 or grade > 5:
        grade = int(input("Введите оценку студента: "))
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO students (name, group_name, grade) VALUES (?, ?, ?)''', (name, group, grade))
    conn.commit()
    print("студент добавлен")

def search_by_group(conn):
    cursor = conn.cursor()
    group_neme = input("Введите имя группы: ")
    cursor.execute('''SELECT * FROM students where group_name = ?''', (group_neme,))
    rows = cursor.fetchall()
    if not rows:
        print("Студенты из такой группы не найдены.")
    else:
        print(f"\nСтуденты группы {group_neme}:")
        for row in rows:
            print(row)
def search_by_grade(conn):
    cursor = conn.cursor()
    grade_seek = int(input("Введите оценку: "))
    cursor.execute('''SELECT * FROM students where grade = ?''', (grade_seek,))
    rows = cursor.fetchall()
    if not rows:
        print("Студенты с такой оценкой не найдены.")
    else:
        print(f"\nСтуденты с оценкой {grade_seek}:")
        for row in rows:
            print(row)

def update_grade(conn):
    cursor = conn.cursor()
    id_seek = int(input("Введите id student: "))
    grade_seek = int(input("Введите оценку: "))
    cursor.execute('''Update students SET grade = ? where id = ?''', (grade_seek, id_seek))
    conn.commit()

    print("оценка изменена")
    cursor.execute('''SELECT * FROM students where grade = ? and id = ?''', (grade_seek, id_seek))
    rows = cursor.fetchall()
    if not rows:
        print("Студенты с такой оценкой не найдены.")
    else:
        print(f"\nСтуденты с оценкой {grade_seek}:")
        for row in rows:
            print(row)

def delete_student(conn):
    cursor = conn.cursor()
    id_seek = int(input("Введите id student: "))
    cursor.execute('''DELETE FROM students where id = ?''', (id_seek,))
    conn.commit()
    print("студент удален")

if __name__ == '__main__':
    main()
