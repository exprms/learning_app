

from server.database import SessionLocal, engine, Base, DB_URL
import sqlalchemy


db = SessionLocal()

m = sqlalchemy.Table('pair', Base.metadata)

s = sqlalchemy.text("select * from pair where id < 10")


x = db.execute(s).fetchall()
print(DB_URL)

# import sqlite3

# try:

# 	# Connect to DB and create a cursor
# 	sqliteConnection = sqlite3.connect('sql.db')
# 	cursor = sqliteConnection.cursor()
# 	print('DB Init')

# 	# Write a query and execute it with cursor
# 	query = 'select sqlite_version();'
# 	cursor.execute(query)

# 	# Fetch and output result
# 	result = cursor.fetchall()
# 	print('SQLite Version is {}'.format(result))

# 	# Close the cursor
# 	cursor.close()

# # Handle errors
# except sqlite3.Error as error:
# 	print('Error occurred - ', error)

# # Close DB Connection irrespective of success
# # or failure
# finally:

# 	if sqliteConnection:
# 		sqliteConnection.close()
# 		print('SQLite Connection closed')
