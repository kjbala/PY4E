# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

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
spannumint=[int(i) for i in spanlst]
print(spannumint)
print('The number of items: ',len(spannumint) )
print('The sum value of the list items: ',sum(spannumint))

    

