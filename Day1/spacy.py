import sys
from collections import Counter

with open(sys.argv[1], "r") as file:
    lines = file.readlines()

a, b = [], []
for line in lines:
    x, y = map(int, line.split())
    a.append(x)
    b.append(y)

a.sort()
b.sort()
d = Counter(b)

s = 0

for ai in a:
    if ai in d:
        s += ai * d[ai]

print(s)
