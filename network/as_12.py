#Sampleinput : http://py4e-data.dr-chuck.net/comments_42.html
#Assignment Url : http://py4e-data.dr-chuck.net/comments_205304.html

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

#Required for the HTTPS url input
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('span')
spanlst=list()
for tag in tags:
    #bs4 the type beauty conversion in to type string
    stringtag=str(tag)
    spannum=re.findall('[0-9]+',stringtag)
    spanlst=spanlst+spannum
spannumint=[int(i) for i in spanlst] #Converting the string type numbered items to int for sum function

print('count: ',len(spannumint) )
print('sum: ',sum(spannumint))