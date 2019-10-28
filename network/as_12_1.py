#Assignment input url : http://py4e-data.dr-chuck.net/known_by_Shannah.html c-7,pos-18 o/p Tammie
#Sample input url : http://py4e-data.dr-chuck.net/known_by_Fikret.html c-4,pos-3 o/p ananyah
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

#Required for the HTTPS url input
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count=0
position=0
url = input('Enter - ')
usrcntinput=int(input('Enter count: '))
usrpos=int(input('Enter position: '))

while True:
    #count=count+1
    html=urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags=soup('a')
    if count==usrcntinput:
        break
    count=count+1
    for tag in tags:
        strtag=tag.get('href',None)
        position=position+1
        if position==usrpos :
            url=strtag
            print(url)
            position=0
            break 