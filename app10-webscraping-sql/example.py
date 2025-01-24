import sqlite3

# make a connection
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# query data some data
cursor.execute("SELECT band, date FROM events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(rows)

# query
cursor.execute("SELECT * FROM events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(rows)

# insert new rows
# new_rows = [('Cats', 'Cat City', '2088.10.17'),
#            ('Hens', 'Hen City', '2088.10.17')]

# cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
# connection.commit()

# query the whole table
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)
