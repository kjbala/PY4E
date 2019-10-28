import urllib.request, urllib.parse, urllib.error
import json
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
jsonlnk = urllib.request.urlopen(url, context=ctx).read()
#print(jsonlnk.decode())
jscont=json.loads(jsonlnk) #Provides 2 dictionary, 
#print(jscont['comments']) #Taking the key comments and getting the list of dictionaries
newlst=jscont['comments']
print(newlst)
lstval=list()
for dicitem in newlst:
    #print(dicitem['count'])
    lstval.append(dicitem['count'])
print(lstval)
print ('Count: ',len(lstval))
print('Sum: ',sum(lstval))
