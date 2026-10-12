import json

with open("tmp.json") as f:
    data = json.load(f)

for k in data.keys():
    k2 = k.replace("data/gh_diffoscope", "data/gh_diffoscope-no-build")
    assert (k != k2)
    with open(k) as f:
        s = f .read()
    with open(k2,"w") as f:
        f.write(s)
