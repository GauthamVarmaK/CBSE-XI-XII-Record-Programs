a=int(input("Enter a three digit number:"))
rev=0
while(a>0):
    rev=(rev*10)+(a%10)
    a//=10
print('Your number in reverse is',rev)
