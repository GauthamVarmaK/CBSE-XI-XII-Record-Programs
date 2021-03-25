import pickle

def insert_row(lst,rollno):
    print(f' Enter Roll Number {rollno} details:')
    name=input('   Name: ')
    marks=int(input('   Marks: '))
    lst.append([rollno,name,marks])

def update_row(lst,rollno,marks): lst[rollno-1][2]=marks

n=int(input('Enter the number of students to be stored: '))
students=[]
for rollno in range(1,n+1): insert_row(students,rollno)
pickle.dump(students,open('students.bin','wb'))
print()
students=pickle.load(open('students.bin','rb'))
rollno=int(input('Enter the roll number to update marks: '))
if 0 < rollno <= len(students):
    marks=int(input('Enter new marks: '))
    update_row(students, rollno, marks)
    print('!!Successfully Updated the records!!')
else: print('Record Not found')
