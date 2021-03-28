content=open('spam_emails.txt','r').read()
words=content.split()
most_occuring_words=['']
for word in set(words):
    if words.count(word)>words.count(most_occuring_words[0]):
        most_occuring_words=[word]
    elif words.count(word)==words.count(most_occuring_words[0]):
        most_occuring_words.append(word)
    else: continue
if len(most_occuring_words)==1:
    print(f'The most commonly occuring word is {most_occuring_words[0]}, which \
occured {words.count(most_occuring_words[0])} times.')
else:
    print('The most commonly occuring words are: ')
    for word in most_occuring_words: print(word)
    print(f'Which occured {words.count(most_occuring_words[0])} times.')