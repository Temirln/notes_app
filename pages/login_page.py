import customtkinter as ctk

from database.crud import get_user, add_user
from tkinter.messagebox import showerror, showinfo, showwarning
from .notes_page import NotePage
from .register_page import RegisterPage


class LoginPage(ctk.CTkFrame):
    def __init__(self, container, user_id, **kwargs):
        super().__init__(container, **kwargs)

        self.container = container

        label = ctk.CTkLabel(self, text="LOGIN")
        label.pack(pady=20)

        frame = ctk.CTkFrame(master=self)
        frame.pack(pady=20, padx=40, fill="both", expand=True)
        
        label = ctk.CTkLabel(master=frame, text="Modern Login System UI")
        label.pack(pady=12, padx=10)

        self.user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username")
        self.user_entry.pack(pady=12, padx=10)

        self.user_pass = ctk.CTkEntry(
            master=frame, placeholder_text="Password", show="*"
        )
        self.user_pass.pack(pady=12, padx=10)

        button = ctk.CTkButton(master=frame, text="Login", command=self.login)
        button.pack(pady=12, padx=10)

        button = ctk.CTkButton(master=frame, text="Sign Up", command=self.move_to_register)
        button.pack(pady=12, padx=10)


    def login(self):

        """
        Функция забирает значения из текстовых полей Логина и Пароля

        Проверяет сперва на пустые поля 

        Если все поля заполнены Проверяет есть ли такой пользователь в базу

        Если Пользователь существует в базе то User переходит на страницу с Заметками        
        """

        
    def move_to_register(self):
        """
        В этой функции вы должны вызвать метод show_page 
        
        чтобы перейти на страницу Регистрации
        """
