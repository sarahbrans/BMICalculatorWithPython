import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="******", database="bmicalc")
mycursor=mydb.cursor()

mycursor.execute("UPDATE bmi_record SET first_name= 'Rafa' WHERE ID=19")
mydb.commit()
mycursor.close()
mydb.close()
