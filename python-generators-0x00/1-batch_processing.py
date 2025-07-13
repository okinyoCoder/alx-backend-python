import mysql.connector

def stream_users_in_batches(batch_size):
    """
    Generator that yields users from the database in batches.
    """
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="45bc67",
            database="ALX_prodev"
        )
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM user_data")
        
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            return batch

        cursor.close()
        mydb.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def batch_processing(batch_size):
    """
    Processes each batch, filtering users over age 25.
    Yields users who meet the age condition.
    """
    for batch in stream_users_in_batches(batch_size):  
        for user in batch: 
            if float(user[3]) > 25:  
                yield user  
