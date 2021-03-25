n = int(input('Enter no. of students: '))
winners = {}
for i in range(0,n):
    name = input('Enter student name: ')
    no_wins = int(input('Enter no. of medals: '))
    winners[name]=no_wins
print('The dictionary is',winners)