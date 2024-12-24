from functools import wraps
from datetime import datetime
import sqlite3


def login_failed(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        call_datetime = datetime.now().isoformat()

        try:
            result = function(args[0], args[1])
            return result
        except ValueError as error:
            with sqlite3.connect("UserManagementDB1-31.db") as connection:
                cursor = connection.cursor()
                cursor.execute("""
                INSERT INTO InvalidUsernameOrPassword(
                                                username,
                                                password,
                                                call_datetime
                                                )
                                                VALUES(
                                                    ?,
                                                    ?,
                                                    ?
                                                );
                """, [username, password, call_datetime])
                connection.commit()

    return wrapper
