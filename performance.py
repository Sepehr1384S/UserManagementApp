from functools import wraps
import time
import sqlite3
from datetime import datetime
from functools import wraps


def performance_recorder(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            return result
        except ValueError as error:
            raise ValueError
        finally:
            stop_time = time.time()
            exec_time = stop_time - start_time
            data = datetime.now().isoformat()

            with sqlite3.connect("UserManagementDB1-31.db") as connection:
                cursor = connection.cursor()
                cursor.execute("""
                INSERT INTO performance (
                                        func_name,
                                        exec_time,
                                        data)
                                        VALUES(?,
                                        ?,
                                        ?); """, [func_name, exec_time, data])

    return wrapper()
