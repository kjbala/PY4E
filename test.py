a=['From:','tst@gmail.com']
c=[]
b=len(a)
print (b)
print(len(c))
import re
numbers="http://www.py4e.com/code3/"
num1=numbers.split('/')
print(num1)
numlist=list()
if numbers=="http://www.py4e.com/code3/":
    num1=numbers.split('/')
    for item2 in num1:
        numbers2=re.findall('[0-9]+',item2)
        numlist.append(numbers2)
print(numlist)