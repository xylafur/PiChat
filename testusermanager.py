
import json
def getUser(username,location):
    name = username
    #print name
    loc = location
    #print loc
    data = {}
    data['username'] = name
    data['longitude'] = location[0]
    data['latitude'] = location[1]
    json_data = json.dumps(data)
    return json_data

username = "Gonzalo"
location = [500, 400]
userlist = []
a = '{"username": "Gonzalo", "latitude": 400, "longitude": 500}'
b = '{"username": "steve", "latitude": 300, "longitude": 600}'
userlist.append(a)
userlist.append(b)
print userlist
print userlist[1]
temp =userlist[1]
variable = json.loads(temp)
print variable["username"]
print userlist[0]
print ""
print userlist[1]
print userlist[1]
# getUser(username, location)
# def addUser(username, location):
#    tempuser = getUser(username, location)
#    print tempuser
#    variable = json.loads(tempuser)
#    print variable["username"]
    #userlist.append(tempuser)
#    userlist.append(tempuser)
    #print type(userlist[0])
    #temp = userlist[0]

#addUser(username, location)
