def sqr(n):
    lst=[]
    for i in range(1,n+1): lst.append(i**2)
    return lst

print("The squares of numbers between 1 and 20 are:",sqr(20),sep='\n')
