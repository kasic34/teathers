from model.user_crud import userCRUD
from model.admin_crud import AdminModel
from view.admin_view import AdminView

class UserPresenter:
    def __init__(self, view):
        self.view = view
        self.user_crud = userCRUD("../student_management.db")

    def create_user(self,username, password, role):
        self.user_crud.create_user(username, password, role)

    def create_course(self, title, description, teacher_id):
        self.user_crud.create_user(title, description, teacher_id)

    def login(self, username, password):
        """ Проверяет логин пользователя и передаёт результат во View """
        user = self.user_crud.get_users(username)

        if user:
            stored_password = user[2] # Пароль в БД
            role = user[3] # Роль пользователя

            if password == stored_password:
                self.view.show_message(f"Добро пожаловать, {username}!")
                self.open_dashboard(role)
            else:
                self.view.show_error("Неверный пароль!")
        else:
            self.view.show_error("Пользователь не найден!")

    def open_dashboard(self, role):

        self.view.show_message(f"Вход выполнен! Роль: {role}")

    def delete_user(self,id):
        self.user_crud.delete_user(id)