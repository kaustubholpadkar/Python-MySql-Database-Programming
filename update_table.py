import MySQLdb

db = MySQLdb.connect('localhost', 'root', 'root', 'python_test_db')

# prepare a cursor object
cursor = db.cursor()

update_statement = """ update student set age = age - 100 """

try:
    cursor.execute(update_statement)
    db.commit()
except Exception as e:
    print('Unable to update data!')
    db.rollback()

db.close()
