import mysql.connector

def stream_users():

    try:
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "45bc67",
            database = "ALX_prodev",
        )
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM user_data")

        for row in cursor:
            yield row
        cursor.close()
        mydb.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None