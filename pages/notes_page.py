from tkinter.messagebox import showerror

import customtkinter as ctk

from database.crud import (
    add_note,
    get_all_notes_by_user,
    get_last_note_id,
    update_note,
    get_user_by_id,
    get_note_by_id,
    delete_note,
)

class NotePage(ctk.CTkFrame):
    def __init__(self, master, user_id, **kwargs):
        super().__init__(master, **kwargs)
        ctk.set_appearance_mode("dark")
        self.user_id = user_id
        self.container = master

        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # Sidebar LEFT FRAME
        self.sidebar = ctk.CTkFrame(self, fg_color="transparent")
        self.sidebar.rowconfigure(3, weight=1)
        self.new_note_btn = ctk.CTkButton(
            self.sidebar,
            text="New Note",
            width=250,
            font=self.winfo_toplevel().button_font,
            command=self.new_note,
        )
        self.new_note_btn.grid(column=0, row=0, padx=10, pady=5)

        self.save_note_btn = ctk.CTkButton(
            self.sidebar,
            text="Save Note",
            width=250,
            fg_color="#307C39",
            hover_color="#245E2B",
            font=self.winfo_toplevel().button_font,
            command=self.save_note,
        )
        self.save_note_btn.grid(column=0, row=1, padx=10, pady=5)

        self.delete_note_btn = ctk.CTkButton(
            self.sidebar,
            text="Delete Note",
            width=250,
            fg_color="#C73E1D",
            hover_color="#8C2D15",
            font=self.winfo_toplevel().button_font,
            command=self.delete_note,
            state="disabled",
        )
        self.delete_note_btn.grid(column=0, row=2, padx=10, pady=5)

        self.notes_list = ctk.CTkScrollableFrame(self.sidebar, fg_color="transparent")
        self.notes_list.grid(column=0, row=3, sticky="nsew")


        self.sidebar.grid(column=0, row=0, padx=(10, 5), pady=10, sticky="ns")



        # Main Window RIGHT FRAME
        self.main_window = ctk.CTkFrame(self,fg_color="transparent")
        
        self.main_window.columnconfigure(0, weight=1)
        self.main_window.rowconfigure(1, weight=1)

        self.user_title = ctk.CTkLabel(
            self.main_window, text="", fg_color="transparent", font=self.winfo_toplevel().title_font
        )
        self.user_title.grid(column=1, row=0, padx=(0, 5), pady=5, sticky="ew")

        self.logout_btn = ctk.CTkButton(self.main_window, command=self.logout)
        self.logout_btn.grid(column=2, row=0, padx=(0, 5), pady=5, sticky="ew")

        self.title = ctk.CTkEntry(
            self.main_window,
            fg_color="transparent",
            border_width=0,
            font=self.winfo_toplevel().title_font,
        )
        self.title.grid(column=0, row=0, padx=(0, 5), pady=5, sticky="ew")

        self.body = ctk.CTkTextbox(
            self.main_window,
            fg_color="transparent",
            font=self.winfo_toplevel().body_font,
            wrap="word",
            activate_scrollbars=False,
        )
        self.body.grid(column=0, row=1, sticky="nsew", columnspan=2)
        
        self.main_window.grid(column=1, row=0, padx=(5, 10), pady=10, sticky="nsew")

        
        
        user = get_user_by_id(self.user_id)
        self.user_title.configure(text=user.login)

        # Immediately Start a New Note
        self.new_note()
        # Load buttons for any existing notes into the sidebar
        self.load_notes()

    def new_note(self):

        self.current_note_id = None
        self.title.delete(0, ctk.END)
        self.body.delete("1.0", ctk.END)
        self.title.insert(0, "New Note")
        self.body.focus_set()
        self.delete_note_btn.configure(state="disabled")

    def save_note(self):
        title = self.title.get()
        body = self.body.get("1.0", ctk.END)

        if self.current_note_id is None:
            add_note(self.user_id, title, body)
        else:
            update_note(self.current_note_id, title, body)

        note_id = get_last_note_id()
        self.current_note_id = note_id

        self.load_notes()
        self.delete_note_btn.configure(state="normal")

    def delete_note(self):
        if self.current_note_id is not None:
            delete_note(self.current_note_id)
            self.load_notes()
            self.new_note()

    def load_note_content(self, note_id):
        note = get_note_by_id(note_id)
        if note:
            note_title = note.title
            note_body = note.content
            self.current_note_id = note_id
            self.title.delete(0, ctk.END)
            self.body.delete("1.0", ctk.END)
            self.title.insert(0, note_title)
            self.body.insert("1.0", note_body)
            self.delete_note_btn.configure(state="normal")

    

    def load_notes(self):
        for child in self.notes_list.winfo_children():
            child.destroy()

        notes = get_all_notes_by_user(self.user_id)
        print(notes)
        for i, note in enumerate(notes):
            note_id = note.note_id
            note_title = note.title

            button = ctk.CTkButton(
                self.notes_list,
                text=note_title,
                width=250,
                fg_color="transparent",
                font=self.winfo_toplevel().button_font,
                command=lambda id=note_id: self.load_note_content(id),
            )
            button.grid(column=0, row=i, padx=10, pady=5)

    def logout(self):
        """
        Функция возвращает пользователя на страницу Авторизации(LoginPage)
        """