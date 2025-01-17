from tkinter import Frame, Label, Entry, Button, messagebox, END
from BusinessLogicLayer.user_business_logic import UserBusinessLogic


class LoginFrame(Frame):
    def __init__(self, main_view, window):
        super().__init__(window)

        self.main_view = main_view

        self.user_business = UserBusinessLogic()

        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="Login Page")
        self.header.grid(row=0, column=1, pady=10, sticky="w")

        self.username_label = Label(self, text="Username")
        self.username_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="w")

        self.username_entry = Entry(self)
        self.username_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.password_label = Label(self, text="Password")
        self.password_label.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="w")

        self.password_entry = Entry(self, show="*")
        self.password_entry.grid(row=2, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.login_button = Button(self, text="Submit", command=self.login)
        self.login_button.grid(row=3, column=1, pady=(0, 10), sticky="w")

        self.register_button = Button(self, text="Register", command=self.show_register_frame)
        self.register_button.grid(row=4, column=1, pady=(0, 10), sticky="w")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            user = self.user_business.login(username, password)

            if user:
                home_frame = self.main_view.switch("home")
                home_frame.set_current_user(user)
                self.username_entry.delete(0, END)
                self.password_entry.delete(0, END)

        except ValueError as error:
            messagebox.showerror(title="User Error", message=error.args[0])

    def show_register_frame(self):
        self.main_view.switch("register")
