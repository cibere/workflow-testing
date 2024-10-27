import json

with open("data.json", "w+") as f:
    before = json.load(f)
    before['release_only'] = True
    json.dump(before, f)