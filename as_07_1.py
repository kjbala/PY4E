# Use the file name mbox-short.txt as the file name
count=0
total=0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line=line.rstrip() # the right strip has removed the white spaces
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos=line.find(':')
    num=line[pos+1:]
    fnum=float(num)
    count=count+1
    total=total+fnum
avg=total/count
print("Average spam confidence:",avg)