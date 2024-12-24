from DataAccessLayer.user_data_access import UserDataAccess
from CommonLayer.performance import performance_recorder


class ActiveOrDeactive:
    @performance_recorder
    def active(self, user):
        user_data_access = UserDataAccess()
        id = []
        for i in user:
            id.append(i[0])

        change = user_data_access.active_user(id)

    @performance_recorder
    def deactive(self, user):
        user_data_access = UserDataAccess()

        id = []

        for i in user:
            id.append(i[0])
        change=user_data_access.deactive_user(id)
