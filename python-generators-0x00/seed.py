import mysql.connector
import csv
import uuid


def connect_db():
    ### connects to the mysql database server ###
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "45bc67",
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
def create_database(connection):
    ### creates the database ALX_prodev if it does not exist ###
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def connect_to_prodev():
    ### connects the the ALX_prodev database in MYSQL ###
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "45bc67",
            database="ALX_prodev",
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    

def create_table(connection):
    ### creates a table user_data if it does not exists with the required fields ###
    try:
        cursor = connection.cursor()
        create_table_query = """
            CREATE TABLE IF NOT EXISTS user_data (
               user_id VARCHAR(36) PRIMARY KEY,
               name VARCHAR(255) NOT NULL,
               email VARCHAR(255) NOT NULL,
               age DECIMAL NOT NULL,
            )
           """
        cursor.execute(create_table_query)
        connection.commit()
        cursor.close()
        print("Table user_data created successfully")
    except mysql.connector.Error as err:
         print(f"Error: {err}")

def insert_data(connection, data):
    ###  inserts data in the database if it does not exist ###
    try:
        cursor = connection.cursor()
        with open(csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Check if record already exists using email
                cursor.execute("SELECT user_id FROM user_data WHERE email = %s", (row['email'],))
                if not cursor.fetchone():
                    user_id = str(uuid.uuid4())
                    cursor.execute(
                        "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                        (user_id, row['name'], row['email'], row['age'])
                    )
        connection.commit()
        cursor.close()
    except (mysql.connector.Error, FileNotFoundError) as err:
        print(f"Error: {err}")