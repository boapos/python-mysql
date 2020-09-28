import mysql.connector

config = {
    'user': 'bob',
    'password': 'Bo74584584747$',
    'host': 'localhost'
}

db = mysql.connector.connect(**config)
cursor =db.cursor()