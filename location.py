import requests, json


#returns longitude and latittude respectively
def getLocation():
    r = requests.get(url='http://freegeoip.net/json/')
    jsonFile = r.json()
    longitude = jsonFile["longitude"]
    latitude = jsonFile["latitude"]
    return [longitude, latitude]
