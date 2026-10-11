import json

def is_dir(package):
    uni = package["unified_diff"]
    if uni is None:
        pass 
    elif type(uni) is str:
        # print(uni,"\n\n", package["path"])
        # exit()
        return False
    else:
        raise Exception()
    
    d = package["details"]
    if d is None:
        raise Exception()
    assert(type(d ) is list)# Supposed to be list of diffs

    
    if len(d) > 1: # can't be multiple unless it's a directory
        for x in d:
            assert(x["source1"].startswith("/tmp/tmp."))
            assert(x["source2"].startswith("/tmp/tmp."))
        return True

    assert(len(d) == 1) # don't think there acn be an empty diff

    data = d[0]
    s1 = data["source1"]
    s2 = data["source2"]
    if s1.startswith("/tmp/tmp."):
        assert (s2.startswith("/tmp/tmp."))
        return True        

    if(s1.startswith("file list")): # the diff is a dir where files are presnt or not
        assert(s2.startswith("file list"))
        return True
    
    # print(s1)

    assert(s1.startswith("Pretty-printed")) # json-formatted, most likely
    assert(s1.startswith("Pretty-printed"))

    # add js-beautify here if needed
    

    return False


def main():
    with open("stats.github.json") as f:
        data = json.load(f)

    dirstats={}
    for k in data :
        
        l = data[k]
        # print(f"k={k}")
        for i, p in enumerate(l):
            # print(p.keys())
            b_tmp = is_dir(p)
            if i > 0:
                assert(b==b_tmp)
            b = b_tmp 
            # print(p.keys())
        
        print(f"k={k}, b={b}")
        dirstats[k] = b 

    print(
        json.dumps(dirstats)
    )


main()