
import os 
import analyse_utils

def json_dir(dirpath:str,maxcount:int =-1)->list:
    fs = os.listdir(dirpath)
    l = []
    for i, f in enumerate(fs):
        if maxcount > -1:
            if i>maxcount:
                break
        p = os.path.join(dirpath, f)
        data = analyse_utils.read_json(p)
        l.append(data)
    return l



res = json_dir("data/gh_diffoscope", 5)
for x in res:
    if type(x) is str:
        continue
    # print(x.keys())
    b1 = x["build1"]
    b2 = x["build2"]
    hpj1 = b1["has_pkg_json"]
    hpj2 = b2["has_pkg_json"]
    assert(hpj1 == hpj2)
    diff  = x["diff"]
    assert (type(diff) is dict)
    repr = True
    if diff:
        repr = False
    print(repr)