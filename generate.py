import json

with open("data.json", "r") as f:
    before = json.load(f)
before['release_only'] = True
with open("data.json", "w") as f:
    json.dump(before, f)