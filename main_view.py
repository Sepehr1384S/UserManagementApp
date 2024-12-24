from .window import Window
from .login import LoginFrame
from .home import HomeFrame
from .user_management import UserManagementFrame
from .register import RegisterFrame


class MainView:
    def __init__(self):
        self.window = Window()

        self.frames = {}

        self.add_frame("register", RegisterFrame(self.window,self))
        self.add_frame("user_management", UserManagementFrame(self.window))
        self.add_frame("home", HomeFrame(self, self.window))
        self.add_frame("login", LoginFrame(self, self.window))

        self.window.show()

    def add_frame(self, name, frame):
        self.frames[name] = frame
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()
        return frame
