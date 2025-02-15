import sqlite3

class course_CRUD:
    def __init__(self, db_path="student_management.db"):
        self.db_patch=db_path

    def create_course(self, title, description, teacher_id):
        conn = sqlite3.connect(self.db_patch)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO courses (title, description, teacher_id) VALUES (?, ?, ?)", (title, description, teacher_id))
        conn.commit()
        conn.close()

    def get_course(self, title):
        conn = sqlite3.connect(self.db_patch)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM courses WHERE title = ?", (title,))
        course = cursor.fetchone()
        conn.close()
        return course

    def update_course_title(self, title):
        conn = sqlite3.connect(self.db_patch)
        cursor = conn.cursor()
        cursor.execute("UPDATE courses WHERE title = ?", (title,))
        conn.commit()
        conn.close()

    def update_course_description(self, description):
        conn = sqlite3.connect(self.db_patch)
        cursor = conn.cursor()
        cursor.execute("UPDATE courses WHERE description = ?", (description,))
        conn.commit()
        conn.close()

    def update_course_teacher_id(self, teacher_id):
        conn = sqlite3.connect(self.db_patch)
        cursor = conn.cursor()
        cursor.execute("UPDATE courses WHERE teacher_id = ?", (teacher_id,))
        conn.commit()
        conn.close()

    def delete_course(self, title):
        conn = sqlite3.connect(self.db_patch)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM courses WHERE title = ?", (title, ))
        conn.commit()
        conn.close()