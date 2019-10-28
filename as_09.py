fname = input("Enter file name: ")
fh = open(fname)
namedict=dict()
newlst=list()
for line in fh:
    line=line.strip()
    if not line.startswith("From:"):
        continue
    listline=line.split()
    newlst.append(listline[1])

for dic in newlst:
    namedict[dic]=namedict.get(dic,0)+1

bigcount=None
bigword=None
for word,count in namedict.items():
    if bigcount is None or count > bigcount:
        bigword=word
        bigcount=count
print(bigword,bigcount)

