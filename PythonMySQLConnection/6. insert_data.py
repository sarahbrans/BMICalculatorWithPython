import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="Heyroot2001!", database="bmicalc")
mycursor=mydb.cursor()

insertrecord="INSERT INTO bmi_record (first_name, weight, height, bmi_value, bmi_category) VALUES (%s, %s, %s, %s, %s)"
record=[
    ('Sarah', 90, 62, 16.46,'underweight'),
    ('John', 75, 68, 11.41,'underweight'),
    ('Emily', 125, 65, 19.92,'normalweight'),
    ('Alex', 130, 75, 16.25,'underweight'),
    ('Adam', 180, 70, 25.82,'overweight' ),
    ('Olivia', 220, 65, 36.61,'severelyobese'),
    ('Ryan', 350, 74, 44.93,'morbidlyobese')
    ]

mycursor.executemany(insertrecord,record)
mydb.commit()