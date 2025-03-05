from model.student_crud import StudentCRUD

class StudentPresenter:
    def __init__(self, view):
        self.view = view
        self.student_crud = StudentCRUD("../student_management.db")


    def delete_student(self,id):
        self.student_crud.delete_student (id)