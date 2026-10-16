import analyse_utils

npm_data = analyse_utils.read_json("stats.npm.json")[".nx"]
github_data = analyse_utils.read_json("stats.github.backup.json")[".nx"]
data = npm_data + github_data
print(github_data)
n = len("--/tmp/tmp.zMD8SddfgO/build/.nx--/tmp/tmp.zMD8SddfgO/build/")
workspace_str = ".nx/workspace-data"
for fp in data:
    pkg = analyse_utils.read_json(fp)
    diff  = pkg["diff"]
    pretty_diff = analyse_utils.diff_recurse(diff)
    for d in pretty_diff:
        jp =d["joined_path"]
        s1 =d["source1"]
        s2=d["source2"]
        # print(jp,s1,s2, sep="   ", end="\n\n")
        # print(jp)
        jp_substr = jp[n:n+len(workspace_str)]
        print(f"jp cmp: sub=\"{jp_substr}\"")
        b = jp_substr == workspace_str
        if not b:
            print(jp,s1,s2, sep="   ", end="\n\n")

