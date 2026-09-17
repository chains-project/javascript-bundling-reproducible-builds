# analyses packages whre yarn.lockwas different

import analyse_utils
lockfile_key = "yarn.lock"

fps_npm = ['data/gh_diffoscope/157_lodash.json',
           'data/gh_diffoscope/225_uri-js.json',
           'data/gh_diffoscope/281_prettier.json',
           'data/gh_diffoscope/319_source-map-js.json',
           'data/gh_diffoscope/328_lodash.merge.json',
           'data/gh_diffoscope/348_gensync.json',
           'data/gh_diffoscope/357_loader-utils.json',
           'data/gh_diffoscope/369_tapable.json',
           'data/gh_diffoscope/371_tsconfig-paths.json',
           'data/gh_diffoscope/473_webpack-sources.json',
           'data/gh_diffoscope/613_dom-accessibility-api.json',
           'data/gh_diffoscope/667_lodash.isplainobject.json',
           'data/gh_diffoscope/721_@webassemblyjs__slash__ast.json',
           'data/gh_diffoscope/728_@webassemblyjs__slash__helper-wasm-bytecode.json',
           'data/gh_diffoscope/738_@webassemblyjs__slash__wast-printer.json',
           'data/gh_diffoscope/739_@webassemblyjs__slash__helper-api-error.json',
           'data/gh_diffoscope/744_@webassemblyjs__slash__wasm-gen.json',
           'data/gh_diffoscope/746_@webassemblyjs__slash__wasm-parser.json',
           'data/gh_diffoscope/748_@webassemblyjs__slash__wasm-edit.json',
           'data/gh_diffoscope/749_@webassemblyjs__slash__helper-buffer.json',
           'data/gh_diffoscope/750_@webassemblyjs__slash__wasm-opt.json',
           'data/gh_diffoscope/751_@webassemblyjs__slash__helper-wasm-section.json',
           'data/gh_diffoscope/757_@webassemblyjs__slash__leb128.json',
           'data/gh_diffoscope/758_@webassemblyjs__slash__ieee754.json',
           'data/gh_diffoscope/759_@webassemblyjs__slash__utf8.json',
           'data/gh_diffoscope/764_lightningcss-linux-x64-musl.json',
           'data/gh_diffoscope/768_@webassemblyjs__slash__floating-point-hex-parser.json',
           'data/gh_diffoscope/797_lodash.debounce.json']

fps_github = ['data/github_projects/196_dragula.json',
              'data/github_projects/203_pug.json',
              'data/github_projects/206_svgo.json',
              'data/github_projects/217_normalizr.json',
              'data/github_projects/219_localtunnel.json',
              'data/github_projects/226_mpvue.json',
              'data/github_projects/245_trix.json',
              'data/github_projects/271_draggable.json',
              'data/github_projects/274_vant-weapp.json',
              'data/github_projects/279_cleave.js.json',
              'data/github_projects/280_FreeTube.json',
              'data/github_projects/290_react-helmet.json']


# fps = fps_github
# fps = fps_npm
fps = fps_github + fps_npm
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
    print(s1, s2)
    details = diff["details"]
    print(details[0]["source1"], details[0]["source2"])
    # print(analyse_utils.show_diff(diff,filenames_only=True))

    hashes1 = b1["stage_hashes"]
    hashes2 = b2["stage_hashes"]
    pre_inst_h1 = hashes1["preinstall_hashes"]
    pre_inst_h2 = hashes2["preinstall_hashes"]
    pre_b_h1 = hashes1["prebuild_hashes"]
    post_h1 = hashes1["post_hashes"]
    post_h2 = hashes2["post_hashes"]
    # print(pre_inst_h1.keys())
    # print(post_h1["package-lock.json"])
    b = print(lockfile_key in pre_inst_h1.keys())
    bo2 = print(lockfile_key in pre_inst_h2.keys())
    assert(lockfile_key in post_h1.keys())
    assert(lockfile_key in post_h2.keys())

    assert (b == bo2)
    if b:
        lockfile_count += 1

print(f"lockfile count {lockfile_count}")
