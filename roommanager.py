import json
import math
import usermanager
class room:
    def __init__(self, initialUser, roomName):
        #initial user will be in the form of a json string
        user = json.loads(initialUser)
        self.longitude = user["longitude"]
        self.latitude = user["latitude"]
        self.users = [initialUser]
        self.text = []
        self.name = roomName
    def addUser(self, userJson):
        self.users.append(userJson)
    def updateText(self, inputText):
        self.text.append(inputText)

allRooms = []

def userWithinRadius(userJson, room):
    #this takes in a a user as a JSON file and parses it
    maxDist = 10
    user = json.loads(userJson)
    userLat = user["latitude"]
    userLon = user["longitude"]

    absLat = math.fabs(userLat - room.latitude)
    absLon = math.fabs(userLon - room.longitude)

    #pythagriam (cant spell) theroem (again math minded lol)
    if( (maxDist * maxDist) >= ( (absLat * absLat) + (absLon * absLon) ) ):
        return True
    else:
        return False

#gonna return a list of all rooms within procimity
def closeRooms(userJson):
    #takes in a JSON of the user
    #use getUser from gonzalo's usermanager to generate a JSON file to compare
    roomsInRadius = []
    for roomElement in allRooms:
        if userWithinRadius(userJson, roomElement):
            roomsInRadius.append(roomElement)
    return roomsInRadius


#function to create a room
def createRoom(userJson, roomName):
    temp = room(userJson, roomName)
    allRooms.append(temp)
