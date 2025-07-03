import mysql.connector

try:
    # Connect to MySQL Server
    connection = mysql.connector.connect(
        host='localhost',        # Replace with your host if different
        user='your_username',    # Replace with your MySQL username
        password='your_password' # Replace with your MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error while connecting to MySQL: {err}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()

