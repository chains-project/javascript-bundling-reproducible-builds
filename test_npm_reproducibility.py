from run import *

if __name__ == "__main__":

    n = 1000
    data = test_stats.get_n_detailed(n)
    # print(data)
    repos = [test_stats.filter_detailed_npm_package_data(x) for x in data]
    for index, _ in enumerate(repos):
        repos[index]["commit"] = None

    print(f"Testing reproducibility status of NPM packages for which data has previously been fetched")
    sbd = "gh_diffoscope"
    test_diffoscope(repos=repos)
    print(f"done: output is in {sbd}")
