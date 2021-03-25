def is_empty(stck): return stck==[]

def push(stck,element): stck.append(element)

def pop(stck): return stck.pop()

def top(stck): return len(stck)-1 if len(stck)>0 else None

def peek(stck): return stck[top(stck)]

def display(stck):
    for element in stck[::-1]: print(f'  {element}')

stck=[]
while True:
    print('===Stack Operations===')
    print(' 1) Push')
    print(' 2) Pop')
    print(' 3) Peek')
    print(' 4) Display')
    print(' 5) Exit')
    opt=input('Enter an option: ')

    if opt=='1':
        push(stck,int(input('Enter element: ')))
    elif opt=='2': 
        if is_empty(stck): print('Underflow! Stack is Empty!!')
        else: print('Popped Item is:',pop(stck))
    elif opt=='3': 
        if is_empty(stck): print('Underflow! Stack is Empty!!')
        else: print('Topmost element is:',peek(stck))
    elif opt=='4': display(stck)
    elif opt=='5': break
    else: print('Invalid Option')
