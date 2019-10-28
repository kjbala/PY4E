# Use the file name mboxshort.txt as the file name
fname = input("Enter file name: ")
count=0
total=0.0
try:
    fh = open(fname)
except:
    print('Invalid File Name', fname)
    quit()
    
for line in fh:
    line=line.rstrip() # the right strip has removed the white spaces
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos=line.find(':')
    #newpos=line.find(' ',pos) # since rstrip is used, it's not required
    num=line[pos+1:]
    fnum=float(num)
    #print(fnum)
    count=count+1
    total=total+fnum
avg=total/count    
print('Done, The average of the values is :', avg)