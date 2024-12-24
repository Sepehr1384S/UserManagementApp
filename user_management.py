from tkinter import Frame, Label, Button, END, messagebox
from tkinter.ttk import Treeview
from BusinessLogicLayer.user_business_logic import UserBusinessLogic
from BusinessLogicLayer.active_or_deactive import ActiveOrDeactive


class UserManagementFrame(Frame):
    def __init__(self, window):
        super().__init__(window)

        self.user_business_logic = UserBusinessLogic()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.header = Label(self, text="User Management")
        self.header.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        self.active_button = Button(self, text="Active", command=self.active_user)
        self.active_button.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="w")

        self.deactive_button = Button(self, text="Deactive", command=self.deactive_user)
        self.deactive_button.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="e")

        columns = ("first_name", "last_name", "username", "status", "role")
        self.table_users = Treeview(self, columns=columns)
        self.table_users.grid(row=2, column=0, columnspan=2, pady=(0, 10), padx=10, sticky="nsew")

        self.table_users.heading("#0", text="NO")
        self.table_users.heading(columns[0], text="First Name")
        self.table_users.heading(columns[1], text="Last Name")
        self.table_users.heading(columns[2], text="Username")
        self.table_users.heading(columns[3], text="Status")
        self.table_users.heading(columns[4], text="Role")

    def active_user(self):
        users = []
        for i in self.table_users.selection():
            for z in self.user:
                if int(i) == z[0]:
                    users.append(z)
                    break
        for i in users:
            if i[4] == 0:
                messagebox.showerror(title="Wrong User", message="Wrong input(You chose wrong User")
                raise ValueError("error")

            self.choise = ActiveOrDeactive()
            self.change = self.choise.active(users)
            self.load_data()

    def deactive_user(self):
        users = []
        for i in self.table_users.selection():
            for z in self.user:
                users.append(z)
                break
        for i in users:
            if i[4] == 1:
                messagebox.showerror(title="Wrong User", message="Wrong input(You chose wrong User")
                raise ValueError("error")
            self.choise2 = ActiveOrDeactive()
            self.change2 = self.choise2.deactive(users)
            self.table_users

    def set_current_user(self, user):
        users = self.user_business_logic.get_users(user)
        self.load_data(users)

    def load_data(self, users):
        row_number = 1
        for user in users:
            self.table_users.insert("", END, iid=user.id, text=row_number,
                                    values=(user.first_name,
                                            user.last_name,
                                            user.username,
                                            "Active" if user.active == 1 else "Deactive",
                                            "Admin" if user.role_id == 1 else "Default User"))

            row_number += 1

        self.table_users.column("#0", width=70, anchor="center")
        self.table_users.column("#1", width=150, anchor="center")
        self.table_users.column("#2", width=150, anchor="center")
        self.table_users.column("#3", width=100, anchor="center")
        self.table_users.column("#4", width=100, anchor="center")
        self.table_users.column("#5", width=100, anchor="center")
