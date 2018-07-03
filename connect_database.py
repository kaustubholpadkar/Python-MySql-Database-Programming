import MySQLdb

# open database connection
db = MySQLdb.connect('localhost', 'root', 'root', 'python_test_db')

# prepare a cursor object
cursor = db.cursor()

# executes SQL query
cursor.execute('select version()')

# fetch single row
data = cursor.fetchone()

# print database version
print('Database version : ' + data[0])

# close database connection
db.close()
