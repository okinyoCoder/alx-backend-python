import functools
import sqlite3
from datetime import datetime
import time

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(*args, **kwargs)
        finally:
            conn.close()
    return wrapper

def  retry_on_failure(retries=3, delay=2):
    def decorators(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_expection = None

            for attempts in range( retries + 1):
                try:
                    return func(*args, **kwargs)
                except sqlite3.OperationalError as e:
                    print(f"Attempt {attempts} failed: {e}")
                    last_expection = e
                    time.sleep(delay)
            return last_expection
        return wrapper
    return decorators


@with_db_connection
@retry_on_failure(retries=3, delay=1)

def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()