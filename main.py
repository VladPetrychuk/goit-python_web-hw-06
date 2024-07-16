import sqlite3
from faker import Faker
import random

fake = Faker()

# Підключення до бази даних SQLite
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Створення таблиць
cursor.execute('''
CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    group_id INTEGER,
    FOREIGN KEY(group_id) REFERENCES groups(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    teacher_id INTEGER,
    FOREIGN KEY(teacher_id) REFERENCES teachers(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject_id INTEGER,
    grade INTEGER,
    date DATE,
    FOREIGN KEY(student_id) REFERENCES students(id),
    FOREIGN KEY(subject_id) REFERENCES subjects(id)
)
''')

conn.commit()

def populate_data():
    # Додавання груп
    groups = [("Group A",), ("Group B",), ("Group C",)]
    cursor.executemany('INSERT INTO groups (name) VALUES (?)', groups)
    
    # Додавання викладачів
    teachers = [(fake.name(),) for _ in range(4)]
    cursor.executemany('INSERT INTO teachers (name) VALUES (?)', teachers)
    
    # Додавання предметів
    subjects = [(fake.word().capitalize(), random.randint(1, 4)) for _ in range(6)]
    cursor.executemany('INSERT INTO subjects (name, teacher_id) VALUES (?, ?)', subjects)
    
    # Додавання студентів
    students = [(fake.name(), random.randint(1, 3)) for _ in range(40)]
    cursor.executemany('INSERT INTO students (name, group_id) VALUES (?, ?)', students)
    
    conn.commit()
    
    # Додавання оцінок студентам
    student_ids = [row[0] for row in cursor.execute('SELECT id FROM students').fetchall()]
    subject_ids = [row[0] for row in cursor.execute('SELECT id FROM subjects').fetchall()]
    
    grades = []
    for _ in range(800):  # До 20 оцінок на кожного студента
        student_id = random.choice(student_ids)
        subject_id = random.choice(subject_ids)
        grade = random.randint(60, 100)
        date = fake.date_between(start_date='-1y', end_date='today')
        grades.append((student_id, subject_id, grade, date))
    
    cursor.executemany('INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)', grades)
    conn.commit()

populate_data()

def execute_and_print(query_file):
    # Зчитування SQL запиту з файлу
    with open(query_file, 'r') as file:
        sql_query = file.read()

    # Виконання SQL запиту
    cursor.execute(sql_query)

    # Отримання результатів
    results = cursor.fetchall()

    # Виведення результатів
    if results:
        for result in results:
            print(result)
    else:
        print("No results found.")

print("Query 1 Results:")
execute_and_print('query_1.sql')

print("\nQuery 2 Results:")
execute_and_print('query_2.sql')

print("\nQuery 3 Results:")
execute_and_print('query_3.sql')

print("\nQuery 4 Results:")
execute_and_print('query_4.sql')

print("\nQuery 5 Results:")
execute_and_print('query_5.sql')

print("\nQuery 6 Results:")
execute_and_print('query_6.sql')

print("\nQuery 7 Results:")
execute_and_print('query_7.sql')

print("\nQuery 8 Results:")
execute_and_print('query_8.sql')

print("\nQuery 9 Results:")
execute_and_print('query_9.sql')

print("\nQuery 10 Results:")
execute_and_print('query_10.sql')

print("\nQuery 11 Results:")
execute_and_print('query_11.sql')

print("\nQuery 12 Results:")
execute_and_print('query_12.sql')