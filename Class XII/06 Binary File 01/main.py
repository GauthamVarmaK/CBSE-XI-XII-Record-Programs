import pickle

print('===Creating a Binary File===')
n=int(input('Enter the number of student details u want to \
store: '))
students={}
for i in range(1,n+1): 
    students[i]=input(f'Enter roll number {i}\'s name: ')
pickle.dump(students,open('students.bin','wb'))
print()
print('===Searching a Binary File===')
students=pickle.load(open('students.bin','rb'))
n=int(input('Enter the roll number to be searched: '))
if n in students: 
    print(f'The name of student whose roll number is {n}, \
is {students[n]}')
else: print('Not found')
