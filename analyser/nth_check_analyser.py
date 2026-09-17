
import analyse_utils 

nth_path = "data/gh_diffoscope/561_nth-check.json"

data = analyse_utils.read_json(nth_path)

c1 = data["build1"]["commit"]
c2 = data["build2"]["commit"]

print(c1, c2)

print(c1 == "debcae5b255d493927bd559f7867748b7e8c53e5")