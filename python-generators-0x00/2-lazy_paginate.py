import mysql.connector

def paginate_users(page_size, offset):
    """
    Fetch one page of users from the database using LIMIT and OFFSET.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  
            database="ALX_prodev"
        )
        cursor = connection.cursor()
        query = "SELECT * FROM user_data LIMIT %s OFFSET %s"
        cursor.execute(query, (page_size, offset))
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        return rows
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []

def lazy_paginate(page_size):
    """
    Generator that lazily fetches pages from the user_data table.
    Only fetches the next page when needed.
    """
    offset = 0
    while True: 
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page  
        offset += page_size
