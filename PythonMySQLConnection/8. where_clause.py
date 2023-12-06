import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="******", database="bmicalc")
mycursor=mydb.cursor()

mycursor.execute("SELECT * FROM bmi_record WHERE bmi_category = 'underweight'")
result= mycursor.fetchall()
for row in result:
    print(row)


mycursor.execute("SELECT * FROM bmi_record WHERE bmi_category = 'morbidlyobese'")
result= mycursor.fetchone()
for row in result:
    print(row)
