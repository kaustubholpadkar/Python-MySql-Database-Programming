import MySQLdb

db = MySQLdb.connect('localhost', 'root', 'root', 'python_test_db')

cursor = db.cursor()

delete_statement = """ delete from student where fname = 'temp1' """

try:
    cursor.execute(delete_statement)
    db.commit()
    print('Data Successfully Deleted')
except Exception as e:
    db.rollback()
    print('Data not Deleted Successfully')

db.close()
