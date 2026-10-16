

import analyse_utils
'''
Nothing new, only jsdom and nth-chech in npm and jsdom in github
'''

fp = "stats.npm.json"
# fp = "stats.github.json"
data = analyse_utils.read_json(fp)["lib"]

print(len(data))
for i,d in enumerate(data):
    # print(d.keys())
    if i ==0 and fp == "stats.npm.json": # jsdom
        continue
    dpath = d["path"]
    print(dpath)

    pdata=analyse_utils.read_json(dpath)
    print(pdata.keys())
    print(pdata["repo"]["clone_url"])
    # break
    # continue
    x = analyse_utils.diff_recurse(d)
    # print(x)
    for elem in x:
        # print(elem)
        jp = elem["joined_path"]
        print(jp)
    print("\n\n")
