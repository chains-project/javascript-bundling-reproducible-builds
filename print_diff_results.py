import os
DIFF_DATADIR="data/gh_diffoscope"
DIFF_DATADIR="data/github_projects"
import json
from lib import utils


def read_data(maxcount=-1):
    DIFF_DATADIR
    fs = os.listdir(DIFF_DATADIR)
    fs.sort(key=lambda x:int(x.split("_")[0]))
    n = len(fs)
    if maxcount > 0:
        n = maxcount
    res = [None]*n
    for i, fp in enumerate([ f"{DIFF_DATADIR}/{f}" for f in fs ]):
        if i >= n:
            break
        print(fp)
        d = utils.read_json(fp)
        if type(d) is dict:
            d["fp"] = fp
        res[i]=d 
       
    return res

    

def filter_diff_results():
    pass


def main():
    data = read_data()
    scount = 0
    for d in data:
        if type(d) is dict:
            diff = d["diff"]
            scount += 1
            if "details" in diff.keys():
                details = diff["details"]
                # print(d.keys())
                print(d["fp"])
                for detail in details:
                    # print(detail.keys())
                    s1 = detail["source1"]
                    s2 = detail["source2"]
                    print( s2,s2)
    
    print(f"total number of completed builds:", scount)

if __name__ == "__main__":
    main()