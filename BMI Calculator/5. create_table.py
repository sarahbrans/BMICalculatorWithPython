import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="Heyroot2001!", database="bmicalc")
mycursor=mydb.cursor()

mycursor.execute("CREATE TABLE bmi_record (id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(20), weight INT, height INT, bmi_value FLOAT, bmi_category VARCHAR(30))")
