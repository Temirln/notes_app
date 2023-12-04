import customtkinter as ctk

from pages.login_page import LoginPage


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x550")
        self.title("Notes with Database")

        self.current_page = None

        self.title_font = ctk.CTkFont(family="Arial", size=40, weight="bold")
        self.body_font = ctk.CTkFont(family="Helvetica", size=16)
        self.button_font = ctk.CTkFont(family="Helvetica", size=13)

        self.show_page(LoginPage)

    def show_page(self, page, id=None):
        if self.current_page:
            self.current_page.destroy()

        self.current_page = page(self, id)
        self.current_page.pack(fill="both", expand=True)

    def show_default_page(self):
        self.show_page(LoginPage)


app = App()
app.mainloop()
