
import json


def read_json(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def extract_diffoscope_diff(data: dict) -> dict:
    return data["diff"]


def diffoscope_diff2list(diffoscope_diff: dict, parent=None) -> list[dict]:
    diffoscope_diff["parent"] = parent

    if not "details" in diffoscope_diff.keys():
        return [diffoscope_diff]
    details = diffoscope_diff["details"]
    assert (type(details) is list)
    diffoscope_diff["details"] = None
    ret = [diffoscope_diff]
    for r in [diffoscope_diff2list(detail, parent=diffoscope_diff) for detail in details]:
        ret += r
    return ret


def diff_recurse(d, joined_path=""):
    res = []
    if d["unified_diff"]:
        res_d = {"joined_path": joined_path}

        for k in ("source1", "source2", "unified_diff"):
            res_d[k] = d[k]
        # res_d["joined_path"] = joined_path + "--" + res_d["source1"]
        res.append(res_d)
    if "details" in d.keys():
        for dd in d["details"]:
            res += diff_recurse(dd, joined_path=joined_path +
                                "--" + dd["source1"])
    return res


def show_diff_from_fp(fp, filenames_only=False):
    diff = extract_diffoscope_diff(
        read_json(fp)
    )
    return show_diff(diff, filenames_only=filenames_only)

def show_diff(diff, filenames_only=False):

    file_diffs = diffoscope_diff2list(diff)

    return "\n".join([d["parent"]["source1"] + "\n" + (d["unified_diff"] + "\n") * (not filenames_only) for d in filter(lambda x: not x["unified_diff"] is None, file_diffs)])


def husky_all():
    # fp = "data-build-investigate/298_cz-cli.json"
    fp = "data-build-investigate/755_protobufjs.json"
    fp = "data/gh_diffoscope/7_ms.json"
    with open("husky.txt") as f:
        fps = [l.strip() for l in f.readlines()]
    for fp in fps:
        if not fp:
            continue
        s = show_diff(fp)
        l = len(s)

        print(fp, l)


def main():
    fp = "data/gh_diffoscope/495_dedent.json"
    print(show_diff_from_fp(fp, True))


if __name__ == "__main__":
    main()
