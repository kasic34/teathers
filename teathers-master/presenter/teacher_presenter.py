from model.teacher_crud import TeacherCRUD


class TeacherPresenter:
    def __init__(self, view):
        self.view = view
        self.teacher_crud = TeacherCRUD("../student_management.db")

    def delete_teacher(self, id):
        self.teacher_crud.delete_teacher(id)

    def create_teacher(self, name, phone, user_id):
        self.teacher_crud.create_teacher(name, phone, user_id)
