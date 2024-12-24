from DataAccessLayer.user_data_access import UserDataAccess
from CommonLayer.performance import performance_recorder
from CommonLayer.login_failed import login_failed

class UserBusinessLogic:
    def __init__(self):
        self.user_data_access = UserDataAccess()


    @performance_recorder
    def login(self, username, password):
        if len(username) < 3 or len(password) < 3:
            raise ValueError("Invalid username or password(3Digit).")

        # Data base

        user = self.user_data_access.get_user(username, password)

        if user:
            if user.active == 1:
                return user
            else:
                raise ValueError("User is not active")
        else:
            raise ValueError("Invalid username or password(Not Found)!")

    def get_users(self, user):
        if user.role_id != 1:
            raise ValueError("Access denied!")

        users = self.user_data_access.get_users(user.id)

        return users
