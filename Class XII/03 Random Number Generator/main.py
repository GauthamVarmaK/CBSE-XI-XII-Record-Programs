import random
roll_again='Yes'
while roll_again=='Yes' or roll_again=='Y':
    print('===Rolling the Dice===')
    print(random.randint(1,6))
    roll_again=input('Roll the dice again [Yes/No]:')
    roll_again=roll_again.title()
