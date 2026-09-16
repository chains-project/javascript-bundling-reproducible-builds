import analyse_utils
import os

BUNDER_NAMES = (
    "Webpack", "Browserify", "Rollup", "Parcel", "Esbuild",
)


def get_scripts(bdata_b):
    pkg_j = bdata_b["package_json"]

    try:
        scripts = pkg_j["scripts"]
    except KeyError as e:
        # print(pkg_j)
        scripts = []
        # raise e
    return scripts


def has_build_sctipt(bdata):

    s1 = get_scripts(bdata["build1"])
    s2 = get_scripts(bdata["build2"])
    b1 = "build" in s1
    b2 = "build" in s2
    # print(f"scripts {s1}")
    assert b1 == b2
    return b1


def get_dev_deps(bdata):

    b1 = bdata["build1"]
    b1_json = b1["package_json"]
    if "devDependencies" in b1_json.keys():
        d1 = b1_json["devDependencies"]
    else:
        d1 = {}

    b2 = bdata["build2"]
    b2_json = b2["package_json"]
    if "devDependencies" in b2_json.keys():
        d2 = b2_json["devDependencies"]
    else:
        d2 = {}

    return d1, d2


def filter_bunder_deps(dev_deps):
    r = []
    for dep_name in dev_deps.keys():
        for bunder_name in BUNDER_NAMES:
            if dep_name.lower() == bunder_name.lower():
                r.append(bunder_name)
                break
    return r


def get_all_json_files(d: str | os.PathLike, max_count=-1) -> list[str]:
    ret = []
    for i, f in enumerate(os.listdir(d)):
        if f.endswith(".json"):
            full_path = os.path.join(d, f)
            ret.append(full_path)
        else:
            print(f"WARN: skipping non-json file {d}/{f}")
        if max_count >= 0 and max_count < i:
            break

    return ret


def count(d):
    total = 0
    bs = 0
    t_data = {"total": {"repro": 0, "nonrepro": 0}, }
    bs_data = {"total": {"repro": 0, "nonrepro": 0}}

    for k in BUNDER_NAMES:
        t_data[k] = {"repro": 0, "nonrepro": 0}
        bs_data[k] = {"repro": 0, "nonrepro": 0}

    for f in get_all_json_files(d):
        # print(f)
        data = analyse_utils.read_json(f)
        # print(type(data))
        if type(data) is str:
            continue
        b = has_build_sctipt(data)
        diff = data["diff"]
        s = str(diff)
        assert (type(diff) is dict)
        diff_size = len(list(diff.keys()))
        reproducible = diff_size == 0
        dev_deps1, dev_deps2 = get_dev_deps(data)
        # print(dev_deps1, dev_deps2)
        bundlers_b1 = filter_bunder_deps(dev_deps1)
        bundlers_b2 = filter_bunder_deps(dev_deps2)
        # print(bundlers_b1, bundlers_b2)
        assert (str(sorted(bundlers_b1)) == str(sorted(bundlers_b2)))
        if reproducible:
            t_data["total"]["repro"]+=1
        else:
            t_data["total"]["nonrepro"]+=1

        for bunder in bundlers_b1:
            if reproducible:
                t_data[bunder]["repro"]+=1
                if has_build_sctipt:
                    bs_data[bunder]["repro"]+=1
            else:

                t_data[bunder]["nonrepro"]+=1
                if has_build_sctipt:
                    bs_data[bunder]["nonrepro"]+=1

        # print(f"diff: {len(list(diff.keys()))}")
        # print(f"{f}:\t{b}")
        if b:
            bs += 1
        total += 1
    # data = [analyse_utils.read_json(f) for f in files]

    # print(data[0]["build1"]["scripts"].keys())
    return {
        "successful": total,
        "script": bs,
        "t_data":t_data,
        "bs_data":bs_data,
    }


def main():
    d1 = "data/gh_diffoscope"
    d2 = "data/github_projects"

    d1data = count(d1)
    print(f"npm registry: {d1data}\n")
    d2data = count(d2)
    print(f"github: {d2data}\n")


if __name__ == "__main__":
    main()
