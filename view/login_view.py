import customtkinter as ctk
from customtkinter import set_default_color_theme, set_appearance_mode

from presenter.login_presenter import UserPresenter
from CTkMessagebox import CTkMessagebox

class login_view(ctk.CTk):
    def __init__(self):
        set_default_color_theme("green")
        set_appearance_mode("dark")
        self.title("Авторизация")
        self.geometry("800x600")

        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 2)

        # Логин
        self.username_entry = ctk.CTkEntry(self, placeholder_text = "Логин")
        self.username_entry.grid(row=0, column=0, padx=5, pady=5)

        # Пароль
        self.password_entry = ctk.CTkEntry(self, placeholder_text = "Пароль")
        self.password_entry.grid(row=0, column=0, padx=5, pady=5)

        # Кнопка входа
        self.login_button = ctk.CTkButton(self, text="Войти")
        self.login_button.grid(row=0, column=0, padx=5, pady=5)

        self.presenter = UserPresenter(self)

    def login(self):
        """Передаем введёгые данные в Presenter"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.presenter.login(username, password)

    def show_message(self, message):
        """Вывод успешного сообщения"""
        CTkMessagebox(title = "Успех", message=message, icon="check")

    def show_error(self, message):
        """Вывод ошибки"""
        CTkMessagebox(title="Ошибка", message=message, icon="cancel")

