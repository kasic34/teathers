from model.course_clud import CourseCRUD

class CoursePresenter:
    def __init__(self, view):
        self.view = view
        self.course_crud = CourseCRUD("../student_management.db")

    def delete_course(self, id):
        self.course_crud.delete_course(id)

    def create_course(self, title, description, teacher_id):
        self.course_crud.create_course(title, description, teacher_id)