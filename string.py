import mysql.connector as conn
mydb = conn.connect(
    host= "localhost",
    user = "root",
    password = '1234'
)

print(mydb)
mycursor =mydb.cursor()
mycursor.execute("CREATE DATABASE mydb ")
mycursor.execute("CREATE TABLE Student (Name VARCHAR(255), Maths INT,Eng INT,Total INT, Grade VARCHAR(255)")

#1ST :
mycursor.execute("SELECT * from Student")

#2nd :
mycursor.execute("SELECT Grade FROM Student WHERE Grade  GROUP BY Grade ")

#3rd :
mycursor.execute("SELECT Names FROM Student WHERE Marks>70 IN Maths")

#4th :
mycursor.execute("SELECT Names FROM Student WHERE GRADE='FAIL' ")