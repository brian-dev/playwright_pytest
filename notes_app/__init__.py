import json


prop_file = './notes_app/props.json'

with open(prop_file, 'r') as f:
    file = json.load(f)

props = file
