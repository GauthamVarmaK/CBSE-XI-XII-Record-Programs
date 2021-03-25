import mysql.connector as sqltor
a=sqltor.connect(host='localhost',user='root',passwd='123456',
                 database='School')
cursor1=a.cursor()
cursor1.execute('SELECT * FROM Student')
data=cursor1.fetchall()
for row in data:
    print(row)
