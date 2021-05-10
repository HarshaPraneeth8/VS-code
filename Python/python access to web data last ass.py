import json

url=input('Enter url:')
import urllib.request, urllib.parse, urllib.error
count = 0


print('Retrieving',url)
uh = urllib.request.urlopen(url).read()


y = json.loads(uh)
for x in y["comments"]:
    n=int(x['count'])
    count= count+n
print('Sum:',count) 