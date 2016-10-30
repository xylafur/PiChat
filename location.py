import requests, json

def getLocation():
    r = requests.get(url='http://freegeoip.net/json/')
    jsonFile = r.json()
    return jsonFile
