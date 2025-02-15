import sqlite3

class teather_CRUD:
    def __init__(self, db_path="student_management.db"):
        self.db_patch = db_path

    def create_teacher(self, name, phone, user_id):
        conn = sqlite3.connect(self.db_patch)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO teachers (name, phone, user_id) VALUES (?, ?, ?, ?)",
                       (name, phone, user_id))
        conn.commit()
        conn.close()

    def get_teacher(self, name):
        conn = sqlite3.connect(self.db_patch)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM teachers WHERE name = ?", (name,))
        teachers = cursor.fetchone()
        conn.close()
        return teachers

    def update_teacher_name(self, name):
        conn = sqlite3.connect(self.db_patch)
        cursor = conn.cursor()
        cursor.execute("UPDATE teachers WHERE name = ?", (name,))
        conn.commit()
        conn.close()

    def update_teacher_phone(self, phone):
        conn = sqlite3.connect(self.db_patch)
        cursor = conn.cursor()
        cursor.execute("UPDATE teachers WHERE phone = ?", (phone,))
        conn.commit()
        conn.close()

    def delete_teacher(self, name):
        conn = sqlite3.connect(self.db_patch)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM teachers WHERE name = ?", (name,))
        conn.commit()
        conn.close()