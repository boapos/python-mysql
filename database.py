import mysql.connector

config = {
    'user': 'bob',
    'password': 'Bob12345678$',
    'host': 'localhost',
    'database': 'acme'
}

db = mysql.connector.connect(**config)
cursor =db.cursor()