import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="Heyroot2001!", database="bmicalc")
mycursor=mydb.cursor()

mycursor.execute("SELECT * FROM bmi_record")
result= mycursor.fetchall()
for row in result:
    print(row)