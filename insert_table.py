import MySQLdb

# open database connection
db = MySQLdb.connect('localhost', 'root', 'root', 'python_test_db')

# prepare a cursor object
cursor = db.cursor()

insert_statement = """ insert into student(fname, lname, age, sex, weight) values ('Kaustubh', 'Olpadkar', 21, 'M', 55) """

try:
    cursor.execute(insert_statement)
    db.commit()
    print('Data Successfully Inserted')
except:
    print('Data Not Inserted')
    db.rollback()

db.close()
