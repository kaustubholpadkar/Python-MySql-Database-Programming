import MySQLdb

# open database connection
db = MySQLdb.connect('localhost', 'root', 'root', 'python_test_db')

# prepare a cursor object
cursor = db.cursor()

sql = """ select * from student where 1=1"""

try:
    cursor.execute(sql)

    table = cursor.fetchall()

    for row in table:
        print(row)

except Exception as e:
    print('Unable to fetch data!')

db.close()
