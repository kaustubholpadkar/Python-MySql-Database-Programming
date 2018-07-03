import MySQLdb

# open database connection
db = MySQLdb.connect('localhost', 'root', 'root', 'python_test_db')

# prepare a cursor object
cursor = db.cursor()

create_statement = """  create table student (
                            fname varchar(50) not null,
                            lname varchar(50) not null,
                            age int,
                            sex varchar(1),
                            weight float
                        ) """

cursor.execute(create_statement)

db.close()
