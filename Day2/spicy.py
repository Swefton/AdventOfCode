import sys

def f(re):
    inc = all(0 < (re[i+1] - re[i]) < 4 for i in range(len(re) - 1))
    dec = all(0 < (re[i] - re[i+1]) < 4 for i in range(len(re) - 1))
    return inc or dec

def m(fn, p2):
    with open(fn, "r") as file:
        lines = file.readlines()

    o = 0

    for line in lines:
        re = list(map(int, line.split()))

        if f(re):
            o += 1
            continue
        
        if p2:
            for i in range(len(re)):
                subre = re[:i] + re[i+1:]
                if f(subre):
                    o += 1
                    break

    print(o)

m(sys.argv[1], False)
