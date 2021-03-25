def is_empty(queue): return queue==[]

def front(queue): return 0 if len(queue)>0 else None

def back(queue): return len(queue)-1 if len(queue)>0 else None

def enqueue(queue,element): queue.append(element)

def dequeue(queue): return queue.pop(front(queue))

def peek(queue): return queue[front(queue)]

def display(queue):
    for element in queue: print(f'  {element}')

queue=[]
while True:
    print('===Queue Operations===')
    print(' 1) Enque')
    print(' 2) Deque')
    print(' 3) Peek')
    print(' 4) Display')
    print(' 5) Exit')
    opt=input('Enter an option: ')

    if opt=='1':
        enqueue(queue,int(input('Enter element: ')))
    elif opt=='2': 
        if is_empty(queue): print('Queue is Empty!!')
        else: print('Dequeued Item is:',dequeue(queue))
    elif opt=='3': 
        if is_empty(queue): print('Queue is Empty!!')
        else: print('Frontmost element is:',peek(queue))
    elif opt=='4': display(queue)
    elif opt=='5': break
    else: print('Invalid Option')
