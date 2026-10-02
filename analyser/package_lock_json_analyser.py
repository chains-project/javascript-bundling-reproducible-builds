import analyse_utils

fps_npm = ['data/gh_diffoscope/40_json-schema-traverse.json',
 'data/gh_diffoscope/98_braces.json',
 'data/gh_diffoscope/156_fast-deep-equal.json',
 'data/gh_diffoscope/256_lines-and-columns.json',
 'data/gh_diffoscope/262_define-property.json',
 'data/gh_diffoscope/344_merge-stream.json',
 'data/gh_diffoscope/358_is-extendable.json',
 'data/gh_diffoscope/495_dedent.json']

fps_github=['data/github_projects/226_mpvue.json',
 'data/github_projects/228_You-Dont-Need-jQuery.json',
 'data/github_projects/243_Mock.json']

# fps = fps_github
fps = fps_npm
lockfile_count = 0
for fp in fps:
    data = analyse_utils.read_json(fp)
    b1 = data["build1"]
    b2 = data["build2"]
    
    hpj1 = b1["has_pkg_json"]
    # print(hpj1)
    diff = data["diff"]
      
    s1 = diff["source1"]
    s2 = diff["source2"]
    print(s1,s2)
    details = diff["details"]
    print(details[0]["source1"], details[0]["source2"])
    # print(analyse_utils.show_diff(diff,filenames_only=True))

    hashes1 = b1["stage_hashes"]
    hashes2 = b2["stage_hashes"]
    pre_inst_h1 = hashes1["preinstall_hashes"]
    pre_inst_h2 = hashes2["preinstall_hashes"]
    pre_b_h1 = hashes1["prebuild_hashes"]
    post_h1 = hashes1["post_hashes"]
    # print(pre_inst_h1.keys())
    # print(post_h1["package-lock.json"])
    b = print("package-lock.json" in pre_inst_h1.keys())
    bo2 = print("package-lock.json" in pre_inst_h2.keys())

    assert(b == bo2)
    if b:
        lockfile_count += 1

print(f"lockfile count {lockfile_count}")