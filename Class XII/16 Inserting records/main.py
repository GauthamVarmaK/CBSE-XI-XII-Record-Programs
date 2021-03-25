import mysql.connector as sqltor
a=sqltor.connect(host='localhost', user='root',passwd='123456',
                 database="Hospital")
cursor1=a.cursor()
cursor1.execute('INSERT INTO Doctor VALUES(1001,"Ganesh","Pune")')
a.commit()
cursor1.execute('SELECT * FROM Doctor')
data=cursor1.fetchall()
for row in data: print(row)