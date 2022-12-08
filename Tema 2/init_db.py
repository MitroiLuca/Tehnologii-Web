import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

current = connection.cursor()

current.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
                ('iPhone 14', 'Price: $800')
                )

current.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
                ('Samsung Galaxy S22 Ultra', 'Price: $1100')
                )

connection.commit()
connection.close()