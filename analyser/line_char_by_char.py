
import sys


with open(sys.argv[1]) as f:
    lines = f.readlines()

i = int(sys.argv[2])
line = lines[i]

for c in line:
    print(c)
