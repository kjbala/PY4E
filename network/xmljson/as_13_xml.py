import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
xmlin = urllib.request.urlopen(url, context=ctx).read()

print(xmlin.decode()) # to print the output in the proper indented xml Format
#print(xmlin) # just prints the output in the sequence order of paragraph

smxml=ET.fromstring(xmlin)
#lstxml=smxml.findall('comments/comment')
#Using a Xpath selector

new=smxml.findall('.//count')
print(new)
newlst=[int(newitem.text) for newitem in new]
print('count:',len(newlst))
print('sum:',sum(newlst))