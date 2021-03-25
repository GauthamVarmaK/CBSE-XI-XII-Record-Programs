lines=open('original.txt','r').readlines()
old_file,new_file=[],[]
for line in lines:
    if line.find('a')!=-1: old_file.append(line)
    else: new_file.append(line)
open('original.txt','w').writelines(old_file)
open('newfile.txt','w').writelines(new_file)
