#!/usr/bin/python3
#from flask import Flask, render_template, request, redirect, url_for
#import location
import json

def getUser(username,location):
    name = username
    print name
    loc = location
    print loc
    data = {}
    data['username'] = name
    data['longitude'] = location[0]
    data['latitude'] = location[1]
    json_data = json.dumps(data)
    return json_data
