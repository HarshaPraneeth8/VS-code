import urllib.request as ur
import xml.etree.ElementTree as ET

url = input('Enter url: ')


total_number = 0
x = 0

print('Retrieving', url)
xml = ur.urlopen(url).read()
print('Retrieved', len(xml), 'characters')

tree = ET.fromstring(xml)
counts = tree.findall('.//count')
for count in counts:
    x += int(count.text)
    total_number += 1

print('Count:', total_number)
print('Sum:', x)