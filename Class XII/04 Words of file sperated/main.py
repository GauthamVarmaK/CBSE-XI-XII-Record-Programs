with open('story.txt') as textfile:
    while True:
        line=textfile.readline()
        if not bool(line): break
        print('#'.join(line.split(' ')),end='')

# execute on idle