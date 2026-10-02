
import analyse_utils

npm_path = "data/gh_diffoscope/551_jsdom.json"

npm_data = analyse_utils.read_json(npm_path)

github_path = 'data/github_projects/216_jsdom.json'

github_data=analyse_utils.read_json(github_path)
print(npm_data.keys())

b1 = npm_data["build1"]
b2 = npm_data["build2"]

# print(b1["commit"])
# print(b2["commit"])

print(github_data["build1"]["commit"])
print(github_data["build2"]["commit"])