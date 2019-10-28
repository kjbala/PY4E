#Picking out the mail ID's

fname = input("Enter file name: ")
fh = open(fname)
count=0
for line in fh:
    line=line.strip()
    if not line.startswith("From:"):
        continue
    listline=line.split()
    count=count+1
    print(listline[1])
print('There were',count,'lines in the file with From as the first word')

