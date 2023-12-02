import sqlite3

connection = sqlite3.connect('db/K-learning.db')
connection.execute('''
    CREATE TABLE IF NOT EXISTS "Users" (
        "id"	INTEGER NOT NULL,
        "email"	TEXT NOT NULL,
        "username"	TEXT NOT NULL,
        "password"	TEXT NOT NULL,
        PRIMARY KEY("id" AUTOINCREMENT)
    );
''')
connection.commit()
cursor = connection.cursor()
