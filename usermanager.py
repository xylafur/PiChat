import json

def getUser(username,location):
    name = username
    loc = location
    data = {}
    data['username'] = name
    data['longitude'] = location[0]
    data['latitude'] = location[1]
    json_data = json.dumps(data)
    return json_data
