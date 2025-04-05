from model.enrollment_crud import enrollmentCRUD

class EnrollmentPresenter:
    def __init__(self, view):
        self.view = view
        self.enrollment_crud = enrollmentCRUD("../student_management.db")

    def delete_enrollment(self, enrollment_id):
        self.enrollment_crud.delete_student_course(enrollment_id)

    def create_enrollment(self, student_id, teacher_id, grade):
        self.enrollment_crud.create_enrollment(student_id, teacher_id, grade)