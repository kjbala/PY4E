fname = input("Enter file name: ")
fh = open(fname)
namedict=dict()
newlst=list()
for line in fh:
    line=line.strip()
    if not line.startswith("From:"):
        continue
    listline=line.split()
    newlst.append(listline[1])  #Good learning skill., the append function after the split and store particular postion in list
print(newlst)
    #newlst=newlst+listline[1]

