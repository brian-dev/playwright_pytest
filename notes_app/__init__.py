import json


prop_file = './notes_app/props.json'
api_file = './notes_app/endpoints.json'

with open(prop_file, 'r') as f:
    props_file = json.load(f)

with open(api_file, 'r') as f:
    endpoints_file = json.load(f)

props = props_file
endpoints = endpoints_file

