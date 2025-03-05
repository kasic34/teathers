import tkinter.ttk
import tkinter.ttk as ttk
import customtkinter as ctk
from presenter.admin_presenter import AdminPresenter


class AdminView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Админ-панель")
        self.geometry("1200x600")

        # Навигация
        self.nav_frame = ctk.CTkFrame(self)
        self.nav_frame.pack(side="left", fill = "y")


        self.students_btn = ctk.CTkButton(self.nav_frame, text="Студенты", command=self.show_students)
        self.students_btn.pack(pady=5, padx=5)

        self.teachers_btn = ctk.CTkButton(self.nav_frame, text="Преподаватели", command=self.show_teachers)
        self.teachers_btn.pack(pady=5, padx=5)

        self.users_btn = ctk.CTkButton(self.nav_frame, text="Пользователи", command=self.show_users)
        self.users_btn.pack(pady=5, padx=5)

        self.courses_btn = ctk.CTkButton(self.nav_frame, text="Курсы", command=self.show_course)
        self.courses_btn.pack(pady=5, padx=5)

        self.enrollments_btn = ctk.CTkButton(self.nav_frame, text="Записи", command=self.show_enrollment)
        self.enrollments_btn.pack(pady=5, padx=5)

        self.reports_btn = ctk.CTkButton(self.nav_frame, text="Отчёты")
        self.reports_btn.pack(pady=5, padx=5)

        self.logout_btn = ctk.CTkButton(self.nav_frame, text="Выход", command=self.exit)
        self.logout_btn.pack(side="bottom", pady=5)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(side="right", expand=True, fill="both")

        self.action_frame = ctk.CTkFrame(self.main_frame)
        self.action_frame.pack(side="bottom", fill="x", pady=10)
        # Презентер без связи с View
        self.add_btn = ctk.CTkButton(self.action_frame, text="Создать")
        self.edit_btn = ctk.CTkButton(self.action_frame, text="Редактировать")
        self.delete_btn = ctk.CTkButton(self.action_frame, text="Удалить", command=self.delete)


        self.presenter = AdminPresenter(self)

    def exit(self):
        self.quit()

    def show_students(self):
        """Вызывает загрузку студентов и отображает их"""
        self.clear_main_frame()
        self.current_table = 'students'
        style = ttk.Style()
        style.configure("Treeview", font=('Arial', '17'))
        style.configure("Treeview.Heading", font=('Arial', '17', 'bold'))
        ctk.CTkLabel(self.main_frame, text="Список студентов", font=("Arial", 20)).pack(pady=10)

        self.tree = ttk.Treeview(self.main_frame, columns=("ID", "Имя", "Возраст", "Телефон", "ID пользователя"),
                                 show="headings")
        self.tree.heading('ID', text='ID', anchor='c')
        self.tree.column('ID', width=50, anchor='c')

        self.tree.heading('Имя', text='Имя', anchor='c')
        self.tree.column('Имя', width=240, anchor='c')

        self.tree.heading('Возраст', text='Возраст', anchor='c')
        self.tree.column('Возраст', width=50, anchor='c')

        self.tree.heading('Телефон', text='Телефон', anchor='c')
        self.tree.column('Телефон', width=120, anchor='c')

        self.tree.heading('ID пользователя', text='ID пользователя', anchor='c')
        self.tree.column('ID пользователя', width=120, anchor='c')

        self.tree.pack(expand=True, fill="both")
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        # Получаем данные из презентера
        students = self.presenter.get_students()

        # Отображаем данные
        self.show_students_data(students)

    def show_students_data(self, students):
        """Отображает список студентов в таблице"""
        self.tree.delete(*self.tree.get_children())

        for row in students:
            self.tree.insert("", "end", values=row)

    def on_select(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            self.delete_btn.pack(side = 'right', padx=5)
            self.edit_btn.pack(side='right', padx=5)
            self.add_btn.pack(side="right", padx=5)

    def edit_student(self):
        selected_item = self.tree.selection()
        if selected_item:
            student_date = self.tree.item(selected_item[0])['values']
            self.tree.delete(selected_item[0])

    def delete(self):
        selected_item = self.tree.selection()
        print(self.current_table)
        if selected_item:
            student_data = self.tree.item(selected_item[0])['values']
            if self.current_table  == 'users':
                from presenter.login_presenter import UserPresenter
                self.current_presenter = UserPresenter(self)
                self.current_presenter.delete_user(student_data[0])
                self.tree.delete(selected_item[0])
            elif self.current_table  == 'students':
                from presenter.student_presenter import StudentPresenter
                self.current_presenter = StudentPresenter(self)
                self.current_presenter.delete_student(student_data[0])
                self.tree.delete(selected_item[0])
            elif self.current_table  == 'teachers':
                print(1)
                from presenter.teacher_presenter import TeacherPresenter
                self.current_presenter = TeacherPresenter(self)
                self.current_presenter.delete_teacher(student_data[0])
                self.tree.delete(selected_item[0])



    def show_teachers(self):
        """Вызывает загрузку студентов и отображает их"""
        self.current_table = 'teachers'
        print(self.current_table)
        self.clear_main_frame()
        style = ttk.Style()
        style.configure("Treeview", font=('Arial', '17'))
        style.configure("Treeview.Heading", font=('Arial', '17', 'bold'))
        ctk.CTkLabel(self.main_frame, text="Список преподователей", font=("Arial", 20)).pack(pady=10)

        self.tree = ttk.Treeview(self.main_frame, columns=("ID", "Имя", "Телефон", "ID пользователя"),
                                 show="headings")
        self.tree.heading('ID', text='ID', anchor='c')
        self.tree.column('ID', width=50, anchor='c')

        self.tree.heading('Имя', text='Имя', anchor='c')
        self.tree.column('Имя', width=240, anchor='c')

        self.tree.heading('Телефон', text='Телефон', anchor='c')
        self.tree.column('Телефон', width=120, anchor='c')

        self.tree.heading('ID пользователя', text='ID пользователя', anchor='c')
        self.tree.column('ID пользователя', width=120, anchor='c')

        self.tree.pack(expand=True, fill="both")
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        # Получаем данные из презентера
        teachers = self.presenter.get_teachers()

        # Отображаем данные
        self.show_teachers_data(teachers)

    def show_teachers_data(self,teachers):
        """Отображает список студентов в таблице"""
        self.tree.delete(*self.tree.get_children())

        for row in teachers:
            self.tree.insert("", "end", values=row)


    def show_course(self):
        """Вызывает загрузку студентов и отображает их"""
        self.current_table = 'course'
        self.clear_main_frame()
        style = ttk.Style()
        style.configure("Treeview", font=('Arial', '17'))
        style.configure("Treeview.Heading", font=('Arial', '17', 'bold'))
        ctk.CTkLabel(self.main_frame, text="Список курсов", font=("Arial", 20)).pack(pady=10)

        self.tree = ttk.Treeview(self.main_frame, columns=("ID", "Название", "Описание", "ID преподавателя"),
                                 show="headings")
        self.tree.heading('ID', text='ID', anchor='c')
        self.tree.column('ID', width=50, anchor='c')

        self.tree.heading('Название', text='Название', anchor='c')
        self.tree.column('Название', width=240, anchor='c')

        self.tree.heading('Описание', text='Описание', anchor='c')
        self.tree.column('Описание', width=120, anchor='c')

        self.tree.heading('ID преподавателя', text='Преподаватель', anchor='c')
        self.tree.column('ID преподавателя', width=120, anchor='c')

        self.tree.pack(expand=True, fill="both")

        # Получаем данные из презентера
        course = self.presenter.get_teachers()
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        # Отображаем данные
        self.show_teachers_data(course)

    def show_course_data(self, course):
        """Отображает список студентов в таблице"""
        self.tree.delete(*self.tree.get_children())
        for row in course:
            self.tree.insert("", "end", values=row)

    def show_enrollment(self):
        """Вызывает загрузку студентов и отображает их"""
        self.current_table = 'enrollments'
        self.clear_main_frame()
        style = ttk.Style()
        style.configure("Treeview", font=('Arial', '17'))
        style.configure("Treeview.Heading", font=('Arial', '17', 'bold'))
        ctk.CTkLabel(self.main_frame, text="Список запесей", font=("Arial", 20)).pack(pady=10)

        self.tree = ttk.Treeview(self.main_frame, columns=("ID", "ID студента", "ID преподавателя", "Оценка"),
                                 show="headings")
        self.tree.heading('ID', text='ID', anchor='c')
        self.tree.column('ID', width=50, anchor='c')

        self.tree.heading('ID студента', text='Студенты', anchor='c')
        self.tree.column('ID студента', width=120, anchor='c')

        self.tree.heading('ID преподавателя', text='Преподаватель', anchor='c')
        self.tree.column('ID преподавателя', width=120, anchor='c')

        self.tree.heading('Оценка', text='Оценки', anchor='c')
        self.tree.column('Оценка', width=50, anchor='c')

        self.tree.pack(expand=True, fill="both")
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        # Получаем данные из презентера
        enrollment = self.presenter.get_teachers()

        # Отображаем данные
        self.show_enrollment_data(enrollment)

    def show_enrollment_data(self, enrollment):
        """Отображает список студентов в таблице"""
        self.tree.delete(*self.tree.get_children())
        print(enrollment)
        for row in enrollment:
            self.tree.insert("", "end", values=row)

    def logout(self):
        pass

    def export_reports(self):
        pass

    def show_users(self):
        """Вызывает загрузку студентов и отображает их"""
        self.current_table = 'users'
        self.clear_main_frame()
        style = ttk.Style()
        style.configure("Treeview", font=('Arial', '17'))
        style.configure("Treeview.Heading", font=('Arial', '17', 'bold'))
        ctk.CTkLabel(self.main_frame, text="Список пользователей", font=("Arial", 20)).pack(pady=10)

        self.tree = ttk.Treeview(self.main_frame, columns=("ID", "Имя", "Пароль", "Роль"),
                                 show="headings")
        self.tree.heading('ID', text='ID', anchor='c')
        self.tree.column('ID', width=50, anchor='c')

        self.tree.heading('Имя', text='Имя', anchor='c')
        self.tree.column('Имя', width=240, anchor='c')

        self.tree.heading('Пароль', text='Пароль', anchor='c')
        self.tree.column('Пароль', width=50, anchor='c')

        self.tree.heading('Роль', text='Роль', anchor='c')
        self.tree.column('Роль', width=120, anchor='c')

        self.tree.pack(expand=True, fill="both")
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        # Получаем данные из презентера
        users = self.presenter.get_users()

        # Отображаем данные
        self.show_users_data(users)

    def show_users_data(self, users):
        """Отображает список студентов в таблице"""
        self.tree.delete(*self.tree.get_children())
        for row in users:
            self.tree.insert("", "end", values=row)

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            if widget != self.action_frame:
                widget.destroy()

if __name__ == "__main__":
    app = AdminView()
    app.mainloop()