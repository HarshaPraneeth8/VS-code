#Enter location: University of Twente
#Retrieving  http://python-data.dr-chuck.net/geojson?#sensor=false&address=University+of+Twente
#Retrieved 2124 characters
#Place id ChIJPZ9qp0tvv4cRb5oLVI9wra8

import urllib.request as ur
import urllib.parse as up
import json

serviceurl = "http://python-data.dr-chuck.net/geojson?"

address_input = input("Enter location: ")
params = {"sensor": "false", "address": address_input}
url = serviceurl + up.urlencode(params)
print("Retrieving ", url)
data = ur.urlopen(url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
json_obj = json.loads(data)

place_id = json_obj["results"][0]["place_id"]
print("Place id", place_id)