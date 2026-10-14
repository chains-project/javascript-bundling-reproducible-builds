
import json 
import sys
import analyse_utils
sys.path.append(".")
from lib import utils 





def path_compare(data):
    x = utils.compare_dirs(data["build1"]["stage_hashes"]["post_hashes"],data["build2"]["stage_hashes"]["post_hashes"])

    x2={}
    for k in x:
        if k!="equal":
            x2[k]=x[k]
    print("cmp res ")
    for k in x2:
        for elem in x2[k]:
            
            print(f"{k}: {elem}")


def main():

    fp = "data/github_projects/201_react-native-web.json"

    with open(fp) as f:
        data = json.load(f)

    diff = data["diff"]
    print(diff.keys())
    print(diff["unified_diff"],diff["source1"])
    details=diff["details"]
    # print(details)
    for d in details:
        print(type(d))
        print(d["source1"])


    x = analyse_utils.diff_recurse(details[1])
    for i,elem in enumerate(x):
        jp = elem["joined_path"]
        ud = elem["unified_diff"]
        print(jp, len(ud),"\n")
        assert type(ud) is str
        outfile = f"diff-react-native-web/{i}.diff"
        with open(outfile,"w") as f:
            f.write(jp + "\n" + ud)

if __name__=="__main__":
    main()