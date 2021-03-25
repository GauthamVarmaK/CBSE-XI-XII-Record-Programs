words=open('spam_emails.txt').read().split()
words.sort()
previous_word,most_occuring='',''
global_count,local_count=0,0
for word in words:
    if (word==previous_word): local_count+=1
    else:
        if local_count>global_count:
            most_occuring=previous_word
            global_count=local_count
        local_count,previous_word=1,word
if local_count>global_count:
    most_occuring,global_count=previous_word,local_count
print(f'"{most_occuring}" is the most occuring word in \
the text file,\nwhich occured {global_count} times.')