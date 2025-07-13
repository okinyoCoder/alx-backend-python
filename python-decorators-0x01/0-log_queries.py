import functools
import mysql.connector
import sqlite3
from datetime import datetime

# Simple decorator to log SQL queries
def log_queries(func):
    @functools.wraps(func)
    def wrapper(query):
        print(f"[SQL] {query}")
        return func(query)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
