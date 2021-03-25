import mysql.connector as sqltor
a=sqltor.connect(host='localhost',user='root',passwd='123456',
                 database='Work')
cursor1=a.cursor()
cursor1.execute('SELECT * FROM EMPLOYEES WHERE City="Delhi"')
record=cursor1.fetchone()
n='Y'
while record != None:
    print(record)
    n=input("Do you want to retrieve another record [Yes/No]: ")
    n=n.capitalize()
    if n!='YES' and n!='Y': break
    record=cursor1.fetchone()
else: print('No more records!')