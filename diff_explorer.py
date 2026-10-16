import json
import sys
from lib import utils
def extract_diff(filepath_in,filepath_out):
    with open(filepath_in) as f:
        czcli = json.load(f)
    
    print(type(czcli))
    print(czcli.keys())
    diff = czcli["diff"]
    print(type(diff))
    print(diff.keys())
    with open(filepath_out,"w") as f:
        json.dump(diff,f)

def diff_recurse(d,joined_path=""):
    res = []
    if d["unified_diff"]:
        res_d = {"joined_path" :joined_path }
        
        for k in ("source1","source2","unified_diff" ):
            res_d [k] = d [k]
        # res_d["joined_path"] = joined_path + "--" + res_d["source1"]
        res.append(res_d)
    if "details" in d.keys():
        for dd in d["details"]:
            res += diff_recurse(dd,joined_path=joined_path + "--" + dd["source1"] )
    return res

def diff(filepath_in):
    with open(filepath_in) as f:
        data = json.load(f)
    print_diff(data)

def print_diff(data):
    print(data.keys())

    res = diff_recurse(data)
    for d in res:
        for k in d.keys():
            print(f"{k}: {d[k]}")
        print()

def main():
    # example for the cz-cli gh repo, which shows interesting result
    # extract_diff("data/github_projects/298_cz-cli.json","298.diff.json")
    # diff("298.diff.json")

    # extract_diff("data/github_projects/253_Fuse.json", "253_Fuse.json")
    # diff("253_Fuse.json")
    # p = "data/gh_diffoscope/551_jsdom.json"
    # p = 'data/github_projects/216_jsdom.json'
    p = "data/gh_diffoscope/561_nth-check.json"
    # p = "data/gh_diffoscope/755_protobufjs.json"
    d = utils.read_json(p)
    print_diff(d["diff"])


if __name__ == "__main__":
    main()