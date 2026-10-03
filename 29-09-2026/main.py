import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    group_name TEXT NOT NULL,
    grade INTEGER NOT NULL,
    age INTEGER
)
""")
conn.commit()


def add_student(name, group_name, grade, age):
    cursor.execute(
        "INSERT INTO students (name, group_name, grade, age) VALUES (?, ?, ?, ?)",
        (name, group_name, grade, age)
    )
    conn.commit()


def show_all():
    cursor.execute("SELECT id, name, group_name, grade, age FROM students")
    rows = cursor.fetchall()
    if not rows:
        print("Список пуст.")
        return
    for r in rows:
        print(f"ID: {r[0]} | ФИО: {r[1]} | Группа: {r[2]} | Оценка: {r[3]} | Возраст: {r[4]}")


def find_by_group(group_name):
    cursor.execute(
        "SELECT id, name, group_name, grade, age FROM students WHERE group_name = ?",
        (group_name,)
    )
    rows = cursor.fetchall()
    if not rows:
        print("Студенты не найдены.")
        return
    for r in rows:
        print(f"ID: {r[0]} | ФИО: {r[1]} | Группа: {r[2]} | Оценка: {r[3]} | Возраст: {r[4]}")


def find_by_grade(grade):
    cursor.execute(
        "SELECT id, name, group_name, grade, age FROM students WHERE grade = ?",
        (grade,)
    )
    rows = cursor.fetchall()
    if not rows:
        print("Студенты не найдены.")
        return
    for r in rows:
        print(f"ID: {r[0]} | ФИО: {r[1]} | Группа: {r[2]} | Оценка: {r[3]} | Возраст: {r[4]}")


def update_grade(student_id, new_grade):
    cursor.execute(
        "UPDATE students SET grade = ? WHERE id = ?",
        (new_grade, student_id)
    )
    conn.commit()
    if cursor.rowcount == 0:
        print("Студент с таким ID не найден.")
    else:
        print("Оценка обновлена.")


def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    if cursor.rowcount == 0:
        print("Студент с таким ID не найден.")
    else:
        print("Студент удалён.")
    show_all()


def average_grade():
    cursor.execute("SELECT AVG(grade) FROM students")
    result = cursor.fetchone()
    if result[0] is None:
        print("Нет данных.")
    else:
        print(f"Средняя оценка: {result[0]:.2f}")


def count_by_group():
    cursor.execute("SELECT group_name, COUNT(*) FROM students GROUP BY group_name")
    rows = cursor.fetchall()
    if not rows:
        print("Нет данных.")
        return
    for r in rows:
        print(f"Группа {r[0]}: {r[1]} чел.")


def top_student():
    cursor.execute("SELECT name, grade FROM students ORDER BY grade DESC LIMIT 1")
    row = cursor.fetchone()
    if row is None:
        print("Нет данных.")
    else:
        print(f"Лучший студент: {row[0]} — оценка {row[1]}")


def older_than(age):
    cursor.execute(
        "SELECT id, name, group_name, grade, age FROM students WHERE age > ?",
        (age,)
    )
    rows = cursor.fetchall()
    if not rows:
        print("Студенты не найдены.")
        return
    for r in rows:
        print(f"ID: {r[0]} | ФИО: {r[1]} | Группа: {r[2]} | Оценка: {r[3]} | Возраст: {r[4]}")


def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Введите целое число.")


def seed_data():
    cursor.execute("SELECT COUNT(*) FROM students")
    if cursor.fetchone()[0] == 0:
        add_student("Иванов Иван", "ИСП-101", 5, 18)
        add_student("Петров Пётр", "ИСП-101", 4, 19)
        add_student("Сидоров Алексей", "ИСП-102", 3, 20)
        add_student("Смирнова Анна", "ИСП-102", 5, 18)
        add_student("Кузнецов Максим", "ИСП-101", 4, 21)


seed_data()

while True:
    print("\n====== УЧЁТКА СТУДЕНТОВ ======")
    print("1. Показать всех студентов")
    print("2. Добавить студента")
    print("3. Найти студентов по группе")
    print("4. Найти студентов по оценке")
    print("5. Изменить оценку")
    print("6. Удалить студента")
    print("7. Средняя оценка")
    print("8. Количество студентов в группах")
    print("9. Студент с самой высокой оценкой")
    print("10. Студенты старше указанного возраста")
    print("0. Выход")

    choice = input("Выберите пункт: ").strip()

    if choice == "1":
        show_all()
    elif choice == "2":
        name = input("ФИО: ").strip()
        group_name = input("Группа: ").strip()
        grade = input_int("Оценка: ")
        age = input_int("Возраст: ")
        add_student(name, group_name, grade, age)
        print("Студент добавлен.")
    elif choice == "3":
        group_name = input("Введите группу: ").strip()
        find_by_group(group_name)
    elif choice == "4":
        grade = input_int("Введите оценку: ")
        find_by_grade(grade)
    elif choice == "5":
        student_id = input_int("Введите ID студента: ")
        new_grade = input_int("Введите новую оценку: ")
        update_grade(student_id, new_grade)
    elif choice == "6":
        student_id = input_int("Введите ID студента: ")
        delete_student(student_id)
    elif choice == "7":
        average_grade()
    elif choice == "8":
        count_by_group()
    elif choice == "9":
        top_student()
    elif choice == "10":
        age = input_int("Введите возраст: ")
        older_than(age)
    elif choice == "0":
        print("Выход.")
        break
    else:
        print("Неверный пункт меню.")

conn.close()