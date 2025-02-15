import sqlite3

class user_CRUD:
    def __init__(self, db_path="student_management.db"):
        self.db_patch=db_path

    def create_user(self, username, password, role):
        conn = sqlite3.connect(self.db_patch)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
        conn.commit()
        conn.close()

    def get_user(self, username):
        conn = sqlite3.connect(self.db_patch)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()
        return user

    def update_password(self, username, new_password):
        conn = sqlite3.connect(self.db_patch)
        cursor = conn.cursor()
        cursor.execute("UPDATE users WHERE username = ? SET password = ?", (username, new_password))
        conn.commit()
        conn.close()

    def delete_user(self, username):
        conn = sqlite3.connect(self.db_patch)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE username = ?", (username, ))
        conn.commit()
        conn.close()