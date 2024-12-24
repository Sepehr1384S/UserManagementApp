class User:
    def __init__(self, id, firstname, lastname, username, password, is_active, role_id):
        self.id = id
        self.first_name = firstname
        self.last_name = lastname
        self.username = username
        self.password = password
        self.active = is_active
        self.role_id = role_id
