import os 
import json 

# D="data/gh_diffoscope"
D="data/github_projects"

files = os.listdir(D)

res = {}
for f in files:
    fp = os.path.join(D,f)
    with open(fp) as f:
        data = json.load(f)
    if type(data) is str:
        continue

    print(f"read {fp}")
    # print(data.keys())
    # print(data["build2"].keys())
    # repo = data["build2"]["repo"]
    commit = data["build2"]["commit"]
    commit1 = data["build1"]["commit"]
    assert commit == commit1
    # repo["commit"]=commit
    # print(repo)
    if "scripts" in data["build1"]["package_json"]:
        scripts = data["build1"]["package_json"]["scripts"].keys()
        if "build" in scripts:
            print (len(list(scripts)))

            # res.append({fp:commit})
            res[fp] = commit
    # try:
    #     l1=data["build1"]["scripts"]
    #     l2=data["build1"]["package_json"]["scripts"]
    #     # print(l1,l2)
    # except:
    #     pass

# with open("tmp-github.json","w") as f:
#     json.dump(res,f)