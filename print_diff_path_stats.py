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
    assert (type(d) is list)  # Supposed to be list of diffs

    if len(d) > 1:  # can't be multiple unless it's a directory
        for x in d:
            tmp_b = x["source1"].startswith(
                "/tmp/tmp.") or x['source1'] == 'file list'
            if not tmp_b:
                print(f"warning: source1={x["source1"]}")
                print(f"FAILING FOR\n##########\n\n{d}\n\n###################")
            assert (tmp_b)

            assert (x["source2"].startswith("/tmp/tmp.")
                    or x['source2'] == 'file list')
        return True

    assert (len(d) == 1)  # don't think there can be an empty diff

    data = d[0]
    s1 = data["source1"]
    s2 = data["source2"]
    if s1.startswith("/tmp/tmp."):
        assert (s2.startswith("/tmp/tmp."))
        return True

    if (s1.startswith("file list")):  # the diff is a dir where files are present or not
        assert (s2.startswith("file list"))
        return True

    # print(s1)

    tmp_b = s1.startswith("Pretty-printed") or s1.startswith("js-beautify")
    if not tmp_b:
        print(f"warning: Pretty-printed!=%{s1}")
        print(f"warning: \"{"%js-beautify {}"}\" != \"{s1}\"")
    assert (tmp_b)  # json-formatted, most likely
    tmp_b = s2.startswith("Pretty-printed") or s2.startswith("js-beautify")
    assert (tmp_b)

    # add js-beautify here if needed

    return False


def check_type():
    fp = "stats.npm.json"
    fp = "stats.github.json"
    with open(fp) as f:
        data = json.load(f)

    dirstats = {}
    for k in data:

        l = data[k]
        # print(f"k={k}")
        for i, p in enumerate(l):
            # print(p.keys())
            b_tmp = is_dir(p)
            if i > 0:
                assert (b == b_tmp)
            b = b_tmp
            # print(p.keys())

        print(f"k={k}, b={b}")
        dirstats[k] = b

    print(
        json.dumps(dirstats)
    )


def get_stats():
    fp = "stats.npm.json"
    fp = "stats.github.json"
    with open(fp) as f:
        data = json.load(f)

    dirstats = {}
    for k in data:

        l = data[k]
        # print(f"k={k}")
        # print(type(l))
        # print(type(l[0]))
        # print(l[0].keys())
        for i in range(len(data[k])):
            data[k][i] = data[k][i]["path"]

    print(
        json.dumps(data)
    )


def main():
    check_type()
    # get_stats()


if __name__ == "__main__":
    main()
