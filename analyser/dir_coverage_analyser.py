

import analyse_utils


fp = "stats.npm.json"
# fp = "stats.github.json"
data = analyse_utils.read_json(fp)["coverage"]

print(len(data))
for d in data:
    # print(d.keys())

    dpath = d["path"]
    print(dpath)

    pdata=analyse_utils.read_json(dpath)
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
