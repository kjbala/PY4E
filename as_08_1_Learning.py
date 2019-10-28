
#Using dictonary to remove duplicates, File name romeo.txt

file=input("Enter the File Name: ")
fh=open(file)
lst=list()
fullword=list()
for line in fh:
    line=line.rstrip()
    word=line.split()
    fullword=fullword+word
print(fullword)
fullword=list(dict.fromkeys(fullword))
fullword.sort()
print(fullword)









 