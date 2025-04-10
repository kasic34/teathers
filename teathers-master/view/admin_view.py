import tkinter.ttk
import tkinter.ttk as ttk
import customtkinter as ctk
from tkinter import simpledialog
from tkinter import filedialog

from model.course_clud import CourseCRUD
from presenter.admin_presenter import AdminPresenter
from presenter.enrollment_presener import EnrollmentPresenter
from presenter.teacher_presenter import TeacherPresenter


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
        self.add_btn = ctk.CTkButton(self.action_frame, text="Создать", command = self.set_add_button)
        self.add_btn.pack(side="right", padx=5)

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

        self.column_mapping = {
            "ID": "id",
            "Имя": "name",
            "Возраст": "age",
            "Телефон": "phone",
            "ID пользователя": "user_id"
        }

        self.tree.pack(expand=True, fill="both")
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        self.tree.bind("<Double-1>", self.on_cell_double_click)
        # Получаем данные из презентера
        students = self.presenter.get_students()

        # Отображаем данные
        self.show_students_data(students)



    def on_cell_double_click(self, event):
        selected_item = self.tree.selection()

        if not selected_item:
            return

        column_id = self.tree.identify_column(event.x)  # Определяем колонку
        column_index = int(column_id[1:]) - 1
        # Получаем индекс (Tkinter считает с 1)
        column_header = self.tree["columns"][column_index]  # Название колонки
        item = self.tree.item(selected_item)
        print(item)
        # Получаем данные строки
        entry_id = item["values"][0]  # ID записи
        old_value = item["values"][column_index]  # Текущее значение ячейки
        column_name = self.column_mapping.get(column_header)
        print(column_name)
        # Запрашиваем новое значение
        new_value = simpledialog.askstring("Редактирование", f"Новое значение для {column_name}:",
                                           initialvalue=old_value)

        if new_value and new_value != old_value:
            self.presenter.update_cell(self.current_table, entry_id, column_name, new_value)

        if self.current_table == 'users':
            users = self.presenter.get_users()
            self.show_users_data(users)
        elif self.current_table == 'students':
            student = self.presenter.get_students()
            self.show_students_data(student)
        elif self.current_table == 'teachers':
            teachers = self.presenter.get_teachers()
            self.show_teachers_data(teachers)
        elif self.current_table == 'courses':
            course = self.presenter.get_courses()
            self.show_course_data(course)
        elif self.current_table=='enrollments':
            enrollments = self.presenter.get_enrollments()
            self.show_enrollment_data(enrollments)


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
                from presenter.teacher_presenter import TeacherPresenter
                self.current_presenter = TeacherPresenter(self)
                self.current_presenter.delete_teacher(student_data[0])
                self.tree.delete(selected_item[0])
            elif self.current_table  == 'courses':
                from presenter.course_presenter import CoursePresenter
                self.current_presenter = CoursePresenter(self)
                self.current_presenter.delete_course(student_data[0])
                self.tree.delete(selected_item[0])
            elif self.current_table  == 'enrollments':
                from presenter.enrollment_presener import EnrollmentPresenter
                self.current_presenter = EnrollmentPresenter(self)
                self.current_presenter.delete_enrollment(student_data[0])
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

        self.column_mapping = {
            "ID": "id",
            "Имя": "name",
            "Телефон": "phone",
            "ID пользователя": "user_id"
        }

        self.tree.pack(expand=True, fill="both")
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        self.tree.bind("<Double-1>", self.on_cell_double_click)
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
        self.current_table = 'courses'
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

        self.column_mapping = {
            "ID": "id",
            "Название": "title",
            "Описание": "description",
            "ID преподавателя": "teacher_id"
        }

        # Получаем данные из презентера
        course = self.presenter.get_courses()
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        self.tree.bind("<Double-1>", self.on_cell_double_click)
        # Отображаем данные
        self.show_course_data(course)

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

        self.column_mapping = {
            "ID": "id",
            "ID студента": "student_id",
            "ID преподавателя": "teacher_id",
            "Оценка": "grade"
        }

        self.tree.pack(expand=True, fill="both")
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        self.tree.bind("<Double-1>", self.on_cell_double_click)
        # Получаем данные из презентера
        enrollment = self.presenter.get_enrollments()

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

        self.column_mapping = {
            "ID": "id",
            "Имя": "username",
            "Пароль": "password",
            "Роль": "role"
        }

        self.tree.pack(expand=True, fill="both")
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        self.tree.bind("<Double-1>", self.on_cell_double_click)
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

    def add_user_window(self):
        ''' интерфейс: поля для ввода и кнопка "сохранить" '''
        add_user = ctk.CTk()
        add_user.title("Админ-панель")
        add_user.geometry("1200x600")
        from presenter.login_presenter import UserPresenter
        self.current_presenter = UserPresenter(self)
        label = ctk.CTkLabel(add_user, text = "Добавить")
        label.pack(pady=10)
        name_entry = ctk.CTkEntry(add_user, placeholder_text = "Имя")
        name_entry.pack(pady=10)
        password_entry = ctk.CTkEntry(add_user, placeholder_text="Пороль")
        password_entry.pack(pady=10)
        role_entry = ctk.CTkEntry(add_user, placeholder_text="Роль")
        role_entry.pack(pady=10)

        def save():
            add_user.withdraw()
            self.current_presenter.create_user(name_entry.get(),password_entry.get(), role_entry.get())
            users = self.presenter.get_users()
            self.show_users_data(users)

        ''' описание кнопки сохранить'''
        save_button = ctk.CTkButton(add_user, text = "Сохранить", command = save)
        save_button.pack(pady=10)
        add_user.mainloop()

    def add_student_window(self):
        ''' интерфейс: поля для ввода и кнопка "сохранить" '''
        add_student = ctk.CTk()
        add_student.title("Админ-панель")
        add_student.geometry("1200x600")
        from presenter.student_presenter import StudentPresenter
        self.current_presenter = StudentPresenter(self)
        label = ctk.CTkLabel(add_student, text = "Добавить")
        label.pack(pady=10)
        name_students_entry = ctk.CTkEntry(add_student, placeholder_text = "Имя")
        name_students_entry.pack(pady=10)
        age_students_entry = ctk.CTkEntry(add_student, placeholder_text="Возраст")
        age_students_entry.pack(pady=10)
        tel_students_entry = ctk.CTkEntry(add_student, placeholder_text="Телефон")
        tel_students_entry.pack(pady=10)
        ID_entry = ctk.CTkEntry(add_student, placeholder_text="ID Пользователя")
        ID_entry.pack(pady=10)

        def save():
            add_student.withdraw()
            self.current_presenter.create_student(name_students_entry.get(), age_students_entry.get(), tel_students_entry.get(), ID_entry.get())
            students = self.presenter.get_students()
            self.show_students_data(students)

        ''' описание кнопки сохранить'''
        save_button = ctk.CTkButton(add_student, text = "Сохранить", command = save)
        save_button.pack(pady=10)
        add_student.mainloop()

    def add_teacher_window(self):
        ''' интерфейс: поля для ввода и кнопка "сохранить" '''
        add_teacher = ctk.CTk()
        add_teacher.title("Админ-панель")
        add_teacher.geometry("1200x600")
        from presenter.teacher_presenter import TeacherPresenter
        self.current_presenter = TeacherPresenter(self)
        label = ctk.CTkLabel(add_teacher, text = "Добавить")
        label.pack(pady=10)
        name_entry = ctk.CTkEntry(add_teacher, placeholder_text = "Имя")
        name_entry.pack(pady=10)
        tel_entry = ctk.CTkEntry(add_teacher, placeholder_text="Телефон")
        tel_entry.pack(pady=10)
        ID_entry = ctk.CTkEntry(add_teacher, placeholder_text="ID Пользователя")
        ID_entry.pack(pady=10)

        def save():
            add_teacher.withdraw()
            self.current_presenter.create_teacher(name_entry.get(),tel_entry.get(), ID_entry.get())
            teachers = self.presenter.get_teachers()
            self.show_users_data(teachers)

        ''' описание кнопки сохранить'''
        save_button = ctk.CTkButton(add_teacher, text = "Сохранить", command = save)
        save_button.pack(pady=10)
        add_teacher.mainloop()

    def add_course_window(self):
        ''' интерфейс: поля для ввода и кнопка "сохранить" '''
        add_course = ctk.CTk()
        add_course.title("Админ-панель")
        add_course.geometry("1200x600")
        from presenter.course_presenter import CoursePresenter
        self.current_presenter = CoursePresenter(self)
        label = ctk.CTkLabel(add_course, text = "Добавить")
        label.pack(pady=10)
        name_entry = ctk.CTkEntry(add_course, placeholder_text = "Название")
        name_entry.pack(pady=10)
        description_entry = ctk.CTkEntry(add_course, placeholder_text="Описание")
        description_entry.pack(pady=10)
        teachers_entry = ctk.CTkEntry(add_course, placeholder_text="Преподователь")
        teachers_entry.pack(pady=10)

        def save():
            add_course.withdraw()
            self.current_presenter.create_course(name_entry.get(), description_entry.get(), teachers_entry.get())
            courses = self.presenter.get_courses()
            self.show_users_data(courses)

        ''' описание кнопки сохранить'''
        save_button = ctk.CTkButton(add_course, text = "Сохранить", command = save)
        save_button.pack(pady=10)
        add_course.mainloop()

    def add_enrollment_window(self):
        ''' интерфейс: поля для ввода и кнопка "сохранить" '''
        add_enrollment = ctk.CTk()
        add_enrollment.title("Админ-панель")
        add_enrollment.geometry("1200x600")
        from presenter.enrollment_presener import EnrollmentPresenter
        self.current_presenter = EnrollmentPresenter(self)
        label = ctk.CTkLabel(add_enrollment, text = "Добавить")
        label.pack(pady = 10)
        students_entry = ctk.CTkEntry(add_enrollment, placeholder_text = "Студент")
        students_entry.pack(pady=10)
        teachers_entry = ctk.CTkEntry(add_enrollment, placeholder_text="Преподователь")
        teachers_entry.pack(pady=10)
        grade_entry = ctk.CTkEntry(add_enrollment, placeholder_text="Оценки")
        grade_entry.pack(pady=10)

        def save():
            add_enrollment.withdraw()
            self.current_presenter.create_enrollment(students_entry.get(), teachers_entry.get(), grade_entry.get())
            enrollment = self.presenter.get_enrollments()
            self.show_users_data(enrollment)

        ''' описание кнопки сохранить'''
        save_button = ctk.CTkButton(add_enrollment, text = "Сохранить", command = save)
        save_button.pack(pady=10)
        add_enrollment.mainloop()

    def set_add_button(self):
        if self.current_table == 'users':
            self.add_user_window()
        elif self.current_table == 'students':
            self.add_student_window()
        elif self.current_table == 'teachers':
            self.add_teacher_window()
        elif self.current_table == 'courses':
            self.add_course_window()
        elif self.current_table=='enrollments':
            self.add_enrollment_window()



if __name__ == "__main__":
    app = AdminView()
    app.mainloop()