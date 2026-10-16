import analyse_utils

f="data/gh_diffoscope/67_@jridgewell__slash__trace-mapping.json"

print(analyse_utils.read_json(f)["diff"])