from DataAccessLayer.user_data_access import UserDataAccess
from CommonLayer.performance import performance_recorder

class Register:
    @performance_recorder
    def register(self,firstname,lastname,username,password):
        data_access=UserDataAccess()
        register=data_access.register(firstname,lastname,username,password)