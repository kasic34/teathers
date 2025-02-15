import sqlite3


class enrllment_CRUD:
    def __init__(self, db_path="student_management.db"):
        self.db_patch = db_path

    def record_student_course(self, student_id, course_id, grade):
        conn = sqlite3.connect(self.db_patch)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO enrollments (student_id, course_id, grade) VALUES (?, ?, ?);", (student_id, course_id, grade))
        conn.commit()
        conn.close()

    def get_course_student(self, student_id, courses_id):
        conn = sqlite3.connect(self.db_patch)
        cursor = conn.cursor()
        cursor.execute("SELECT courses.* FROM enrollments JOIN courses ON enrollments.course_id = courses.id WHERE enrollments.student_id = ?", (student_id, courses_id))
        course_student = cursor.fetchone()
        conn.close()
        return course_student

    def update_estimation_student(self, student_id, courses_id):
        conn = sqlite3.connect(self.db_patch)
        cursor = conn.cursor()
        cursor.execute("UPDATE enrollments SET grade = ? WHERE student_id = ? AND course_id = ?", (student_id, courses_id))
        conn.commit()
        conn.close()


    def delete_student_course(self, student_id, courses_id):
        conn = sqlite3.connect(self.db_patch)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM enrollments WHERE student_id = ? AND course_id = ?", (student_id, courses_id))
        conn.commit()
        conn.close()