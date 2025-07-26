import functools
import time
import sqlite3

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('user.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

def cache_query(func):
    functools.wraps(func)
    def wrapper(conn, query, *args, kwargs):
        if query in query_cache:
            print("using cached.")
            return query_cache[query]
        else:
            result = func(conn, query, *args, **kwargs)
            query_cache[query] = result
            print("Query executed and cached.")
            return result
    return wrapper
        
@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")