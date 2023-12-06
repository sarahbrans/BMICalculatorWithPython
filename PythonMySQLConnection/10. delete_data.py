import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="******", database="bmicalc")
mycursor=mydb.cursor()

mycursor.execute("DELETE bmi_record WHERE ID = '20'")
