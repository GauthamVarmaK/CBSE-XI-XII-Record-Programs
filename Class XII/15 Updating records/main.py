import mysql.connector as sqltor
a=sqltor.connect(host='localhost', user='root',passwd='123456',
                 database="Work")
cursor1=a.cursor()
cursor1.execute("UPDATE Employees SET Age=60 WHERE Name \
LIKE 'A%'")
a.commit()
print('Updated Records!!')
cursor1.execute('SELECT * FROM Employees WHERE Name \
LIKE "A%"')
data=cursor1.fetchall()
for row in data: print(row)