import mysql.connector


try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345"
    )
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit(1)

cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")