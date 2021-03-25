def primes():
    primes_list=[]
    for i in range(0,51):
        if i==0 or i==1: continue
        for prime in primes_list:
            if i%prime==0: break
        else: primes_list.append(i)
    for prime in primes_list: print(prime)

primes()
