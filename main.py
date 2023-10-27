import json
from fastapi import FastAPI
import re
import requests
import os
import dbm
import kv

app = FastAPI()

cache = {}
shortenURLs = False


if 'HOST_URL' in os.environ:
    host_url = os.environ['HOST_URL'] + "/g"
else:
    host_url = None


def lookUpIP(ip):
    sourceSites = [f"https://ipwhois.app/json/{ip}",f"https://json.geoiplookup.io/{ip}"]
    result = (requests.get(f"https://json.geoiplookup.io/{ip}"))
    if result.status_code == 200:
        return result
    


@app.get("/lookupIP")
def generate(ip):
    if kv.keyExists(ip):
        print(f"Returning {ip} from local cache.")
        return  json.loads(kv.getValue(ip))
    else:
        result = lookUpIP(ip)
        print("new",result)
        kv.addKey(ip,json.dumps(result.json()))
        print(f"Resolving {ip} and adding to local cache.")
        return result.json()
    
