import urllib.request, urllib.parse, urllib.error
import json
import ssl

url = "http://python-data.dr-chuck.net/geojson?"
add = input('Enter location:')

parameters = {"sensor": "false", "address": add}
paramsurl = urllib.parse.urlencode(parameters)


queryurl = url + paramsurl
print("Retrieving ", queryurl)


data = urllib.request.urlopen(queryurl).read().decode()


jsondata = json.loads((data))
place_id = jsondata["results"][0]["place_id"]
print("Place id ", place_id)