p=int(input('Enter principle amount '))
t=float(input('Enter time period '))
r=float(input('Enter the rate of interest '))
si=(p*t*r)/100
ci=p*((1+(r/100))**t)
print('Simple interest is',si)
print('Compound interest is',ci)