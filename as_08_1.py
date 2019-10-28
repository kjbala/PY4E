file=input("Enter the File Name: ")
fh=open(file)
lst=list()
for line in fh:
    line=line.rstrip()
    word=line.split()
    for w in word:
        if w in lst:
            continue
        lst.append(w)
lst.sort()
print(lst)