#Tuples Assignment- Chapter 10

fname=input("Enter the File Name: ")
try:
    fh=open(fname)
except:
    print("Invalid File name",fname)
    quit()
#fh=fh.strip(), not working shows a trace back error
lst=list()
nlst=list()
for line in fh:
    line=line.strip()
    if not line.startswith("From"):
       continue
    lst=line.split()
    if len(lst)!=7: # using the lenght command to filter out the From: which has only 2 items
        continue
    nlst.append(lst[5])
print(nlst)



