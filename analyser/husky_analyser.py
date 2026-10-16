
import analyse_utils

def all_diff():
    npm_stats = analyse_utils.read_json("stats.npm.json")
    github_stats = analyse_utils.read_json("stats.github.json")
    husky_paths = npm_stats[".husky"]
    pathstats = {}
    for p in husky_paths:
        print(f"stats for {p}:")
        data = analyse_utils.read_json(p)
        diff = data["diff"]
        build1 = data["build1"]
        build2 = data["build2"]
        build1_post_hashes = build1["stage_hashes"]["post_hashes"]
        build2_post_hashes = build2["stage_hashes"]["post_hashes"]

        for filepath in build1_post_hashes:
            if filepath.startswith("node_modules") or filepath.startswith(".git"):
                continue
            if not filepath in build2_post_hashes:
                print(f"build 1 only: \"{filepath}\"")
                if filepath in pathstats:
                    pathstats[filepath]+=1
                else:
                    pathstats[filepath]=1

        for filepath in build2_post_hashes:
            if filepath.startswith("node_modules") or filepath.startswith(".git"):
                continue
            if not filepath in build1_post_hashes:
                print(f"build 2 only: \"{filepath}\"")
        # break
        print()
        continue
        pretty_diff = analyse_utils.diff_recurse(diff)
        for x in pretty_diff:
            # print(x["unified_diff"])
            if not ".husky" in x["joined_path"]:
                continue
            print(x["unified_diff"])
        print()
        # break
    for p in pathstats:
        print(p, pathstats[p])

def ms():
    data = analyse_utils.read_json('data/gh_diffoscope/7_ms.json')
    h = data["build2"]["stage_hashes"]
    print(type(h))
    print(h.keys())
    h = h["post_hashes"]
    for hi in h:
        if ".husky" in hi:
            print(hi)
def main():
    ms()
if __name__=="__main__":
    main()
