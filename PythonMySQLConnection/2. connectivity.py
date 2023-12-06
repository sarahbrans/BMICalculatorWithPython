import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="******")
print(mydb)

#to see if connection has been established:
if(mydb):
    print("connection successful")
else:
    print("connection unsuccessful")


