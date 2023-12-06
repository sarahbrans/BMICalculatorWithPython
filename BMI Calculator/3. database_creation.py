import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="Heyroot2001!")
mycursor=mydb.cursor()

mycursor.execute("CREATE DATABASE bmicalc")
