from model.admin_crud import AdminModel

class AdminPresenter:

    def __init__(self,view):
        self.admin_crud = AdminModel('../student_management.db')
        self.view = view

    def get_students(self):
        return self.admin_crud.get_students()

    def get_teachers(self):
        return self.admin_crud.get_teachers()

    def get_users(self):
        return self.admin_crud.get_users()

    def get_courses(self):
        return self.admin_crud.get_courses()

    def get_enrollments(self):
        return self.admin_crud.get_enrollments()

    def update_cell(self, table, entry_id, column, new_value):
        self.admin_crud.update_cell(table, entry_id, column, new_value)