import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="Heyroot2001!")
print(mydb)

#to see if connection has been established:
if(mydb):
    print("connection successful")
else:
    print("connection unsuccessful")


