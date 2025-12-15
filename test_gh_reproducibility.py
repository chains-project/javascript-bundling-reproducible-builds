from run import *

if __name__ == "__main__":
    print(f"Testing reproducibility status of Github projects for which data has previously been fetched")
    sbd = "github_projects"
    test_diffoscope(diffoscope_subdir=sbd)
    print(f"done: output is in {sbd}")
