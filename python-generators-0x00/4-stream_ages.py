import mysql.connector

def stream_user_ages():
    """
    Generator that yields ages one at a time from user_data table.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ALX_prodev"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT age FROM user_data")
        
        for (age,) in cursor:
            yield float(age)

        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def compute_average_age():
    """
    Uses stream_user_ages to compute the average without loading all data.
    """
    total = 0
    count = 0
    for age in stream_user_ages():
        total += age
        count += 1

    if count > 0:
        print(f"Average age of users: {total / count:.2f}")
    else:
        print("No user data found.")

if __name__ == "__main__":
    compute_average_age()
