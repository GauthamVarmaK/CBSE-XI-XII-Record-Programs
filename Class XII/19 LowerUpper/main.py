def checkuplow(sentence):
    upper,lower=0,0
    for letter in sentence:
        if letter.isupper(): upper+=1
        elif letter.islower(): lower+=1
    print("The number of upper case letters in the sentence is:",
          upper)
    print("The number of lower case letters in the sentence is:",
          lower)

sentence=input("Enter your Sentence: ")
checkuplow(sentence)
