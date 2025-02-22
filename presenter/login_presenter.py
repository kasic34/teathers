from model.user_crud import userCRUD
from model.admin_crud import AdminModel
from view.admin_view import AdminView

class UserPresenter:
    def __init__(self, view):
        self.view = view
        self.user_crud = userCRUD("model/student_management.db")

    def login(self, username, password):
        """ Проверяет логин пользователя и передаёт результат во View """
        user = self.user_crud.get_user(username)

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