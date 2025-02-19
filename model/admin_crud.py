
import sqlite3

class AdminModel:
    def __init__(self, db_path="../student_management.db"):
        self.db_path = db_path


    def get_students(self):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        result =cursor.fetchall()
        connection.close()
        return result

    def get_teachers(self):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM teachers")
        result = cursor.fetchall()
        connection.close()
        return result

    def get_courses(self):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM courses")
        result = cursor.fetchall()
        connection.close()
        return result


    def get_enrollments(self):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM enrollments")
        result = cursor.fetchall()
        connection.close()
        return result