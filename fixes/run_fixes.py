import sys
import os
sys.path.append("../")
sys.path.append(".")


if True:
    import run
    from lib import utils


def build_jsdom(d=None):

    patch_path = os.path.join(os.path.dirname(
        __file__), "jsdom-fixes", "fix.patch")

    repo = {
        "name": "jsdom",
        "clone_url": "https://github.com/jsdom/jsdom.git",
        "commit": "adb999a12912f2f5ceb49fde6b1c9f7051968dc8",
        "patches": [{"patch": patch_path, "subdir": ""}]
    }

    container_ids = (
        "rb-24.4.1-alpine:latest",
        "localhost/rb-lts-jod:latest",
    )

    assert os.path.isfile(patch_path)

    # data = utils.build(
    #     url=url, commit=commit, patches=[], log_shell=True, rmwork=True, verbose=False, tmpdir=tmpdir
    # )

    if not type(d) is str:
        d = repo["name"]

    data = run.test_diffoscope([repo], d, container_ids=container_ids)
    print(data)


def build_probufjs(d=None):

    patch_path = os.path.join(os.path.dirname(
        __file__), "protobufjs-fixes", "fix.patch")

    repo = {
        "name": "protobufjs",
        "clone_url": "https://github.com/protobufjs/protobuf.js",
        "commit": "827ff8e48253e9041f19ac81168aa046dbdfb041",
        "patches": [{"patch": patch_path, "subdir": ""}]
    }

    # container_ids=(
    #           "rb-24.4.1-alpine:latest",
    #          "localhost/rb-lts-jod:latest",
    # )

    assert os.path.isfile(patch_path)

    if not type(d) is str:
        d = repo["name"]

    run.test_diffoscope([repo], d,)


def build_cz_cli(d=None):

    patch_path = os.path.join(os.path.dirname(
        __file__), "cz-cli-fixes", "fix.patch")

    postinstall_patch_path = os.path.join(os.path.dirname(
        __file__), "cz-cli-fixes",
        #   "babel-plugin-istanbul.patch"
        #   "i2.patch"
        "i3.patch"
    )

    repo = {
        "name": "cz-cli",
        "clone_url": "https://github.com/commitizen/cz-cli",
        "commit": "3c08866d9a8788c25798035f2dee7feaa6c03287",
        # "patches": [{"patch": patch_path, "subdir": ""}],
        "postinstall_patches": [{"patch": postinstall_patch_path, "subdir": "node_modules/babel-plugin-istanbul"}],
    }

    # container_ids=(
    #           "rb-24.4.1-alpine:latest",
    #          "localhost/rb-lts-jod:latest",
    # )

    assert os.path.isfile(patch_path)

    if not type(d) is str:
        d = repo["name"]

    run.test_diffoscope([repo], d, rmwork=False)


def main():
    d = "fixes-tmp"
    # build_jsdom(d)
    # build_probufjs(d)
    # build_cz_cli(d)
    build_cz_cli(d + "-cz-cli-i3")


if __name__ == "__main__":
    main()
