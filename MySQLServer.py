import mysql.connector



db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345"
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")