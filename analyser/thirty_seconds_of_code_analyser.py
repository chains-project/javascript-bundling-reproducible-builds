
import analyse_utils

fp ="data/github_projects/5_30-seconds-of-code.json"

data = analyse_utils.read_json(fp)

diff = data["diff"]

print(len(diff))

x = analyse_utils.diff_recurse(diff)

for elem in x:
    p = elem["joined_path"]
    print(p)
    # print(elem.keys())
    # sprint(elem["unified_diff"])