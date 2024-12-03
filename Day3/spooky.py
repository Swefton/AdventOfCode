
import re
import sys

def m(fn):
    with open(fn, "r") as file:
        lines = file.readlines()
    dop = r"do\(\)"
    nop = r"don't\(\)"
    mulp = r"mul\((\d+),\s*(\d+)\)"
    full_seq = r"do\(\)|don't\(\)|mul\(\d+,\s*\d+\)"
    f = True

    s = 0
    for line in lines:
        tks = re.findall(full_seq, line)
        for tk in tks:
            if re.match(dop, tk):
                f = True
            elif re.match(nop, tk):
                f = False
            elif re.match(mulp, tk) and f:
                x, y = map(int, re.findall(r"\d+", tk))
                s += x * y
        
    print(s)

m(sys.argv[1])
