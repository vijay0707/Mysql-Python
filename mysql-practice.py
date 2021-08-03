import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd ='pass',
    database="test_pydb"
    )

cur = mydb.cursor()

#-----------------------------------------------------------
# Creating Db and table: 

# cur.execute("CREATE DATABASE test_pydb")

# cur.execute("SHOW DATABASES")

# for db in cur:
#     print(db)

# cur.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")

# cur.execute("SHOW TABLES")

# for tb in cur:
#     print(tb)

# ------------------------------------------------------------
# Inserting Values:

# sqlFormula = "INSERT INTO students (name,age) VALUES (%s, %s)"
# students = [("Karan", 18),("Saran", 21),
#             ("Kumar", 20),("Joke", 23)] # single value=single tuple without array

# cur.executemany(sqlFormula, students) #For single value use execute 

# mydb.commit()

# -------------------------------------------------------------
# Selecting and getting data:

# cur.execute("SELECT name,age FROM students")

# result = cur.fetchall()   #fetches the result

# for row in result:
#     print(row)

# result = cur.fetchone()
# print(result)

#----------------------------------------------------------------
# Query conditions

# sql = "SELECT name,age FROM students WHERE age > 20"
# sql = "SELECT name,age FROM students WHERE name LIKE 'S%'"
# sql = "SELECT name,age FROM students WHERE name LIKE '%ar%'"

# cur.execute(sql)
# result = cur.fetchall()
# for row in result:
#     print(row)

#-----------------------------------------------------------------
# Update and limit

# sql = "UPDATE students SET age = 17 WHERE name = 'Joke'"
# cur.execute(sql)
# mydb.commit()

# sql = "SELECT * FROM students LIMIT 2"
# cur.execute(sql)
# result = cur.fetchall()
# for row in result:
#     print(row)

#-----------------------------------------------------------------
# Ordering Queries and Results

# sql = "SELECT name,age FROM students ORDER BY age"
# sql = "SELECT name,age FROM students ORDER BY name DESC"
# cur.execute(sql)
# result = cur.fetchall()
# for row in result:
#     print(row)

#-----------------------------------------------------------------
# Deleting Entries and Dropping Tables

# sql = "DELETE FROM students WHERE name = 'kumar'"
# sql = "DROP TABLE students"
# sql = "DROP TABLE IF EXISTS students"

# cur.execute(sql)
# mydb.commit()




