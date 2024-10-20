import getpass
import mysql.connector
from mysql.connector import Error
def Create_Database():
    try:
        username = input("Enter the username:")
        password = getpass.getpass("Enter your password: ")
        connection = mysql.connector.connect(
            host = "localhost",
            password = password,
            username = username
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXIST alx_book_store")
            print (f"Database 'alx_book_store' created successfully!")
    except mysql.connector.Error:
        print (f"I can not connect to my SQL")
    
    except Error as e:
        print (e)

    finally:
        if connection.is_connected():
            cursor.closed()
            connection.closed()
            print (f"The connection has been closed")
                
if __name__ == "__main__":
    Create_Database()








