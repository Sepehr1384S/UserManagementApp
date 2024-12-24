from tkinter import Frame, Label, Button


class HomeFrame(Frame):
    def __init__(self, main_view, window):
        super().__init__(window)

        self.main_view = main_view

        self.grid_columnconfigure(0, weight=1)

        self.header = Label(self)
        self.header.grid(row=0, column=0, pady=10, padx=10)

        self.logout_button = Button(self, text="Logout", command=self.logout)
        self.logout_button.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="ew")

    def logout(self):
        self.main_view.switch("login")

    def set_current_user(self, user):
        self.current_user = user
        self.header.config(text=f"Welcome {user.first_name} {user.last_name}")

        if user.role_id == 1:
            self.user_management_button = Button(self, text="User Management", command=self.show_user_management)
            self.user_management_button.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="ew")

    def show_user_management(self):
        user_management_frame = self.main_view.switch("user_management")
        user_management_frame.set_current_user(self.current_user)
