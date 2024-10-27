import json

with open("data.json", "r") as f:
    before = json.load(f)
before['release_only'] = True
ver = before['Version']
major, minor, micro = ver.split(".")
micro = int(micro) + 1
before['Version'] = f"{major}.{minor}.{micro}"
with open("data.json", "w") as f:
    json.dump(before, f)