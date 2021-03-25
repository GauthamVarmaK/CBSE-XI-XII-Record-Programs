alphacount=lowercount=vowelcount=0
vowels='aAeEiIoOuU'
letters=list(open('projectreport.txt').read())
for letter in letters:
    if letter.isalpha():
        alphacount+=1
        if letter.islower(): lowercount+=1
        if letter in vowels: vowelcount+=1

print(f'The total number of vowels is: {vowelcount}')
print(f'The total number of consonants is: {alphacount-vowelcount}')
print(f'The total number of upper case characters is: {alphacount-lowercount}')
print(f'The total number of lower case characters is: {lowercount}')
