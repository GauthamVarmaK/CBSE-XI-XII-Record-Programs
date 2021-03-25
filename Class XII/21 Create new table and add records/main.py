import mysql.connector as sqltor
a=sqltor.connect(host='localhost', user='root',passwd='123456',
                 database="School")
cursor1=a.cursor()
cursor1.execute('CREATE TABLE STUDENT_MARKS (RollNo INT \
PRIMARY KEY,Name VARCHAR(50) NOT NULL,Marks INT NOT NULL)')
for i in range(1,6):
    name=input("Enter the student's name: ")
    roll=int(input("Enter the student's roll number: "))
    marks=int(input("Enter the student's Marks: "))
    cursor1.execute(f'INSERT INTO STUDENT_MARKS VALUES({roll},"{name}",{marks})')
    a.commit()
cursor1.execute('SELECT * FROM STUDENT_MARKS')
data=cursor1.fetchall()
for row in data:
    print(row)