from model.teacher_crud import TeacherCRUD


class TeacherPresenter:
    def __init__(self, view):
        self.view = view
        self.teacher_crud = TeacherCRUD("../student_management.db")

    def delete_teacher(self, id):
        self.teacher_crud.delete_teacher(id)

    def create_teacher(self,name, phone, user_id):
        self.teacher_crud.create_teacher(name, phone, user_id)

    def create_user(self, username, password, role):
        self.user_crud.create_user(username, password, role)

    def create_student(self,name, age, phone, user_id):
        self.student_crud.create_student(name, age, phone, user_id)

    def create_course(self, title, description, teacher_id):
        self.course_crud.create_course(self, title, description, teacher_id)