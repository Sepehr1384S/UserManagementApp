from tkinter import Frame, Label, Entry, Button, END
from BusinessLogicLayer.register_business import Register


class RegisterFrame(Frame):
    def __init__(self, window, mainviewer):
        super().__init__(window)
        self.main_view = mainviewer

        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="Register Page")
        self.header.grid(row=0, column=1, pady=10, sticky="w")

        self.username_label = Label(self, text="Username")
        self.username_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="w")

        self.username_entry = Entry(self)
        self.username_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.password_label = Label(self, text="Password")
        self.password_label.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="w")

        self.password_entry = Entry(self, show="*")
        self.password_entry.grid(row=2, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.firstname_label = Label(self, text="First Name")
        self.firstname_label.grid(row=3, column=0, pady=(0, 10), padx=10, sticky="w")

        self.firstname_entry = Entry(self)
        self.firstname_entry.grid(row=3, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.lastname_label = Label(self, text="Last Name")
        self.lastname_label.grid(row=4, column=0, pady=(0, 10), padx=10, sticky="w")

        self.lastname_entry = Entry(self)
        self.lastname_entry.grid(row=4, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.register_button = Button(self, text="Register", command=self.register_user)
        self.register_button.grid(row=5, column=1, pady=(0, 10), sticky="w")

        self.back_button = Button(self, text="Back", command=self.back)
        self.back_button.grid(row=6, column=1, pady=(0, 10), sticky="w")

    def register_user(self):
        if len(self.username_entry.get()) > 3 and len(self.lastname_entry.get()) > 3 and len(
                self.firstname_entry.get()) > 3 and len(self.password_entry.get()) > 3:
            register_instance = Register()
            register = register_instance.register(self.lastname_entry.get(), self.firstname_entry.get(),
                                                  self.username_entry.get(), self.password_entry.get())
            self.password_entry.delete(0, END)
            self.lastname_entry.delete(0, END)
            self.firstname_entry.delete(0, END)
            self.username_entry.delete(0, END)
            self.main_view.switch("login")

    def back(self):
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.firstname_entry.delete(0, END)
        self.lastname_entry.delete(0, END)
        self.main_view.switch("login")
