

import analyse_utils


data = analyse_utils.read_json("/home/user1/skola/javascript-bundling-reproducible-builds/stats.github.json")["packages"]

print(len(data))
for d in data:
    # print(d.keys())
    print(d["path"])

    pdata=analyse_utils.read_json(d["path"])
    print(pdata["repo"]["clone_url"])
    # break
    x = analyse_utils.diff_recurse(d)
    # print(x)
    for elem in x:
        # print(elem)
        jp = elem["joined_path"]
        print(jp)
    print("\n\n")
