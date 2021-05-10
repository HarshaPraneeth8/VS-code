import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore SSL certificate errors
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode= ssl.CERT_NONE

url= input('Enter- ')
html=urllib.request.urlopen(url, context=ctx).read()
soup=BeautifulSoup(html,'html.parser')

sum=0
tags=soup('span')

for tag in tags:
    sum=sum+int(tag.contents[0])

print(sum)
