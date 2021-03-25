def div7n5():
    lst=[]
    for i in range(1000,3001):
        if ((i%7)==0) and ((i%5)!=0): lst.append(i)
    return lst

print("The list of numbers divisible 7 but not 5, between \
1000 and 3000 are:",div7n5())
