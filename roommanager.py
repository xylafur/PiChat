import json
import math
import usermanager
class room:
    def __init__(self, initialUser):
        #initial user will be in the form of a json string
        user = json.loads(initialUser)
        self.longitude = user["longitude"]
        self.latitude = user["latitude"]
        self.users = [initialUser]
        self.text = []
    def addUser(self, userJson):
        self.users.append(userJson)
    def updateText(self, inputText):
        self.text.append(inputText)

def userWithinRadius(userDict, room):
    maxDist = 10
    user = json.loads(userDict)
    userLat = user["latitude"]
    userLon = user["longitude"]

    absLat = math.fabs(userLat - room.latitude)
    absLon = math.fabs(userLon - room.longitude)

    #pythagriam (cant spell) theroem (again math minded lol)
    if( (maxDist * maxDist) >= ( (absLat * absLat) + (absLon * absLon) ) ):
        return True
    else:
        return False
