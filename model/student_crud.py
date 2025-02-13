import sqlite3

class student_CRUD:
    def __init__(self, db_path="student_management.db"):
        self.db_patch=db_path

    def create_student(self, name, age, phone, user_id):
        conn = sqlite3.connect(self.db_patch)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, age, phone, user_id) VALUES (?, ?, ?, ?)", (name, age, phone, user_id))
        conn.commit()
        conn.close()

    def get_student(self, name):
        conn = sqlite3.connect(self.db_patch)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
        student = cursor.fetchone()
        conn.close()
        return student

    def update_student_name(self, name):
        conn = sqlite3.connect(self.db_patch)
        cursor = conn.cursor()
        cursor.execute("UPDATE students WHERE name = ?", (name,))
        conn.commit()
        conn.close()

    def update_student_age(self, age):
        conn = sqlite3.connect(self.db_patch)
        cursor = conn.cursor()
        cursor.execute("UPDATE students WHERE age = ?", (age,))
        conn.commit()
        conn.close()

    def update_student_phone(self, phone):
        conn = sqlite3.connect(self.db_patch)
        cursor = conn.cursor()
        cursor.execute("UPDATE students WHERE phone = ?", (phone,))
        conn.commit()
        conn.close()

    def delete_student(self, name):
        conn = sqlite3.connect(self.db_patch)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE name = ?", (name, ))
        conn.commit()
        conn.close()