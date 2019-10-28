import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
xmlin = urllib.request.urlopen(url, context=ctx).read()
#decodedlin=xmlin.decode()
print(xmlin.decode()) # to print the output in the proper indented xml Format
#print(xmlin) # just prints the output in the sequence order of paragraph

smxml=ET.fromstring(xmlin)
lstxml=smxml.findall('comments/comment')
numlst=list()
for itlst in lstxml:
    print('name: ',itlst.find('name').text)
    print('count: ',itlst.find('count').text)
    numlst.append(itlst.find('count').text)

print('The List Values: ', numlst)
newlst=[int(i) for i in numlst]
print(sum(newlst))
