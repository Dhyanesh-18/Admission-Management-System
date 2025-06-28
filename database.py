import sqlite3
def create_database():
    connection = sqlite3.connect('DB.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS applications (
        name TEXT,
        father_name TEXT,
        age INTEGER,
        cutoff INTEGER,
        caste TEXT,
        course TEXT,
        roll_no INTEGER
    )
    ''')
    connection.commit()
    connection.close()
def insert_application(name, father_name, age,cutoff, caste, course, roll_no):
    connection = sqlite3.connect('DB.db')
    cursor = connection.cursor()
    cursor.execute('''
    INSERT INTO applications (name, father_name, age,cutoff, caste, course, roll_no)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (name, father_name, age, cutoff, caste, course, roll_no))
    connection.commit()
    connection.close()

