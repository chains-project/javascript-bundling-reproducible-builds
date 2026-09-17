
import matplotlib.pyplot as plt
import print_diff_results
from lib import utils
import json
import pickle
import os


def read_and_process_data(diff_datadir, maxcount=-1, ):

    fs = os.listdir(diff_datadir)
    fs.sort(key=lambda x: int(x.split("_")[0]))
    n = len(fs)
    if maxcount > 0:
        n = maxcount
    res = [None] * n
    for i, fp in enumerate([f"{diff_datadir}/{f}" for f in fs]):
        if i >= n:
            break
        print(fp)
        d = utils.read_json(fp)
        if type(d) is dict:
            d = d["diff"]
        res[i] = {
            "fp": fp,
            "d": d,
        }

    return res
# data = read_and_process_data(diff_datadir=print_diff_results.NPM_DIFF_DATADIR)
# with open("stats.data.npm.json", "w") as f:
#     json.dump(data, f)
# exit()

# with open("stats.data.npm.json", "r") as f:
#     data = json.load(f)


# with open("stats.data.npm.pickle", "wb") as f:
#     pickle.dump(data, f)

with open("stats.data.npm.pickle", "rb") as f:
    data = pickle.load(f)


# exit()
buildfails = 0
difffails = 0
reproducible = 0
nonreproducible = 0

for dm in data:
    d = dm["d"]
    if type(d) is str:
        if d == "buildfail":
            buildfails += 1
        elif d == "difffail":
            difffails += 1
        else:
            raise Exception(f"unknown {d}")
    elif type(d) is dict:
        if not d:
            reproducible += 1
        else:
            nonreproducible += 1
    else:
        raise Exception(f"unknow type: {type(d)} for d = {d}")

print(f"buildfails={buildfails}")
print(f"difffails={difffails}")
print(f"reproducible={reproducible}")
print(f"nonreproducible={nonreproducible}")


plt.bar(["R", "NR", "fail"], [reproducible, nonreproducible, buildfails])
plt.show()
