import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

url=input('enter url:')
count=int(input('eneter count:'))
pos=int(input('enter position:'))-1
htm=urllib.urlopen(url).read()

soup=BeautifulSoup(htm,'htm.parser')
href=soup('a')

for x in range(count):
    link = href[pos].get('href', None)
    print(href[pos].contents[0])
    htm = urllib.urlopen(link).read()
    soup = BeautifulSoup(htm,"htm.parser")
    href = soup('a')
   
