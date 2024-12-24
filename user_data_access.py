import sqlite3
from CommonLayer.user import User


class UserDataAccess:
    def get_user(self, username, password):
        with sqlite3.connect("UserManagementDB1-31.db") as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
SELECT id,
       first_name,
       last_name,
       username,
       active,
       role_id
FROM   User
Where  username = ?
AND    password = ?
""", [username, password]).fetchone()

            if data:
                user = User(data[0], data[1], data[2], data[3], None, data[4], data[5])
                return user

    def get_users(self, user_id):
        users = []
        with sqlite3.connect("UserManagementDB1-31.db") as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
        SELECT id,
               first_name,
               last_name,
               username,
               active,
               role_id
        FROM   User
        Where  id   !=  ?
        """, [user_id]).fetchall()

            for item in data:
                user = User(item[0], item[1], item[2], item[3], None, item[4], item[5])
                users.append(user)

        return users

    def active_user(self, id):
        for i in id:
            with sqlite3.connect("UserManagementDB1-31.db") as connection:
                cursor = connection.cursor()
                data = cursor.execute(f"""
                                    UPDATE user
                                    SET is_Active = ?
                                    WEHRE id = ?;""", [0, i])
                connection.commit()

    def deactive_user(self, id):
        for i in id:
            with sqlite3.connect("UserManagementDB1-31.db") as connection:
                cursor = connection.cursor()
                data = cursor.execute("""
                UPDATE user 
                SET is_active 
                WHERE id = ?;""", [1, i])
                connection.commit()

    def register(self, firstname, lastname, username, password):
        with sqlite3.connect("UserManagementDB1-31.db") as connection:
            curser = connection.cursor()
            curser.execute(f"""
            INSERT INTO user
            (first_name,
            last_name,
            username,
            password)
            VALUES (
            '{firstname}',
            '{lastname}',
            '{username}',
            '{password}');""")
            connection.commit()
