import mysql.connector as myconn 

def connect():
    return myconn.connect(
        host="localhost",
        user="root",
        password="1234",
        database="bank_system"
    )