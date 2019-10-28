#Tuples Assignment- Chapter 10

fname=input("Enter the File Name: ")
try:
    fh=open(fname)
except:
    print("Invalid File name",fname)
    quit()
#fh=fh.strip(), not working shows a trace back error

hrdic=dict()
for line in fh:
    line=line.strip()
    if len(line)<40 or not line.startswith('From'): #the string pattern.,  can use and operator also.
       continue
    nline=line.split()
    time=nline[5] # Storing the time in the string format
    #print(type(time))
    hr=time.split(':') # Splitting the hr with delimeter, outputs the string in list :
    #hr=time.strip(":"), should chekc this out.
    if not hr[0] in hrdic or hr[0] in hrdic:
        hrdic[hr[0]]=hrdic.get(hr[0],0)+1
print(hrdic)

# Tuple Getting started
tuplehr=hrdic.items() #Dictionary.items gives tuple
for k,v in sorted(tuplehr):
    print(k,v)

#Alternate method, Compression Method... #Optional way
print(sorted([(k,v) for k,v in tuplehr]))  # sorted by keys
print(sorted([(v,k) for k,v in tuplehr])) #sorted by values