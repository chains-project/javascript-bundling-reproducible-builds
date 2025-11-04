from stats import stats
import subprocess
# import pandas as pd
import pickle
import json
import os

DATA_DIR = "data"
# DATA_DIR="data_clean"


def dump_all():
    pkgs = stats.get_all_package_info()

    with open(f"{DATA_DIR}/all.pickle", "wb") as f:
        pickle.dump(pkgs, f)


def read_all():

    with open(f"{DATA_DIR}/all.pickle", "rb") as f:
        data = pickle.load(f)

    return data


def dump_most_popular():
    all_pkgs = read_all()
    top_pkgs = stats.get_most_popular_packages(all_pkgs, min_downloads=100)

    with open(f"{DATA_DIR}/min100.pickle", "wb") as f:
        pickle.dump(top_pkgs, f)
    print(top_pkgs)


def fetch_detailed_for_all():
    # dump_all()
    # dump_most_popular()
    # exit()
    with open(f"{DATA_DIR}/min100.pickle", "rb") as f:
        pkgs = pickle.load(f)

    # pkg = pkgs[0]
    # print(pkgs)
    #
    detailed = []
    n = len(pkgs)
    for index, pkg in enumerate(pkgs):
        name = pkg["name"]
        print(f"fetching {index}/{n} (name={name})")
        # fp = f"{DATA_DIR}/min100detailed-by-index/min100detailed-{index}.pickle"
        fpj = f"{DATA_DIR}/min100detailed-by-index/min100detailed-{index}.pickle"

        if os.path.exists(fpj):
            continue
        try:

            data = stats.get_detailed_stats(name)
        except KeyboardInterrupt as e:
            raise e
        except:
            data = {"name": name, "status": "failed"}
        detailed.append(data)

        # with open(fp, "wb") as f:
        #     pickle.dump(data, f)
        with open(fpj, "w") as f:
            json.dump(data, f)
        # break

    # with open(f"{DATA_DIR}/min100detailed.pickle", "wb") as f:
    #     pickle.dump(detailed, f)


def get_min100_brief():
    with open(f"{DATA_DIR}/min100.pickle", "rb") as f:
        pkgs = pickle.load(f)
        return pkgs


def write_detailed_to_single_file():
    pkgs = get_min100_brief()
    detailed = []
    os.makedirs(f"{DATA_DIR}/min100detailed-by-index", exist_ok=True)

    n = len(pkgs)
    for index, pkg in enumerate(pkgs):
        name = pkg["name"]
        fp = f"{DATA_DIR}/min100detailed-by-index/min100detailed-{index}.pickle"

        with open(fp, "rb") as f:
            try:
                data = pickle.load(f)
            except EOFError as e:
                if os.path.exists(fp):
                    print(f"failed to read {fp}")
                    subprocess.run(["rm", fp], check=True)
                # raise e
                data = None
        detailed.append(data)

    with open(f"{DATA_DIR}/min100detailed.pickle", "wb") as f:
        pickle.dump(detailed, f)


def get_n_detailed(n):
    """
    Get detailed information about n packages. The information must have been fetched previously
    """
    #
    pkgs = get_min100_brief()

    detailed = []

    for index, pkg in enumerate(pkgs):
        name = pkg["name"]
        # fp = f"{DATA_DIR}/min100detailed-by-index/min100detailed-{index}.pickle"
        fpj = f"{DATA_DIR}/min100detailed-by-index/min100detailed-{index}.json"
        # os.rename(fp, fpj)
        with open(fpj, "rb") as f:
            data = json.load(f)
        # with open(fpj, "w") as f:
        #     json.dump(data, f)
        detailed.append(data)
        if index > n:
            break

    return detailed


def remove_git_prefix(repo_url: str, remote_check_s) -> str:
    if repo_url.startswith(remote_check_s + "http"):
        repo_url = repo_url[len(remote_check_s):]

    return repo_url


def filter_detailed_npm_package_data(elem):
    """
    Takes npm data as input and returns a dict with keys name, repository and commit
    """
    # TODO: type may not be git

    remote_check_s = "remote-git+"
    git_check_s = "git+"
    try:
        if "repository" in elem.keys():
            rds = elem["repository"]
            if type(rds) is dict:
                repository = rds["url"]
                repository = remove_git_prefix(repository, remote_check_s)
                repository = remove_git_prefix(repository, git_check_s)
            elif type(rds) is str:
                repository = rds
            else:
                # TODO: is this possible? Raise exception maybe
                repository = rds
        else:
            repository = None

        if "gitHead" in elem.keys():
            commit = elem["gitHead"]
        elif "_rev" in elem.keys():
            commit = elem["_rev"]
        else:
            commit = None
        name = elem["name"]
        # if repository is None:
        #     print("\n",elem,"\n")
        #     print(name)
        #     raise Exception()
    except Exception as e:
        print(elem, "\nKEYS:", elem.keys())
        raise e
    return {
        "name": name,
        "clone_url": repository,
        "commit": commit,
        "npm_data": elem,
    }


if __name__ == "__main__":
    # dump_all()
    # dump_most_popular()
    fetch_detailed_for_all()
    data = get_n_detailed(1000)
    write_detailed_to_single_file()

    for elem in data:
        d = filter_detailed_npm_package_data(elem)
        print(d)
