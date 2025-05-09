
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

    def get_users(self):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
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

    def db_delete(self, name):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE name = ?", (name, ))
        conn.commit()
        conn.close()

    def update_cell(self, table, entry_id, column, new_value):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute(f"UPDATE {table} SET {column} = ? WHERE id = ?", (new_value, entry_id))
        connection.commit()
        connection.close()
