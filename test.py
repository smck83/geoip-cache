import requests
import json

result = (requests.get("https://json.geoiplookup.io/8.8.8.8"))
print(result.json()['isp'])