import re
file=input("Enter the file name: ")
try:
    fh=open(file)
except:
    print("Invalid File name:",file)
    quit()
numlist=list()
for line in fh:
    line=line.strip()
    splitspace=line.split()
    if len(splitspace)<1: #Removing Blank Lines
        continue
    for item in splitspace:
        numbers=re.findall('[0-9]+',item)                  
        if item=="http://www.py4e.com/code3/":
            num1=item.split('/')
            for item2 in num1:
                numbers2=re.findall('[0-9]+',item2)
                #numlist.append(numbers2) #Creates list within list, since the re has already o/ps list
                numlist=numlist+numbers2 #to avoid list within list, also doesn't adds blank values.
        elif len(numbers)!=0:
            #numlist.append(numbers)
            numlist=numlist+numbers

            
print(numlist,'\n')
intlist=list()
for stringitem in numlist:
    intitem=int(stringitem) #Converting the list items in the string format to integer format
    intlist.append(intitem)
print("The number of items in the list is: ",len(intlist))
print('\nThe total of the number of the items in the list is: ',sum(intlist))