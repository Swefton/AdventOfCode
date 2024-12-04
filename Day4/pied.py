import re
import sys

def p1(gr, w="XMAS"):
    rs = len(gr)
    cs = len(gr[0])
    l = len(w)
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    
    def ch(x, y):
        return 0 <= x < rs and 0 <= y < cs

    def find(x, y, dx, dy):
        for i in range(l):
            nx, ny = x + i * dx, y + i * dy
            if not ch(nx, ny) or gr[nx][ny] != w[i]:
                return False
        return True

    out = 0
    for x in range(rs):
        for y in range(cs):
            for dx, dy in dir:
                if find(x, y, dx, dy):
                    out += 1
    return out
    
def p2(gr):
    rs = len(gr)
    cs = len(gr[0])
    out = 0

    def ch(sequence):
        return sequence == "MAS" or sequence == "SAM"

    for i in range(1, rs - 1):
        for j in range(1, cs - 1):
            tl = gr[i - 1][j - 1]
            tr = gr[i - 1][j + 1]
            bl = gr[i + 1][j - 1]
            br = gr[i + 1][j + 1]
            c = gr[i][j]

            d1 = tl + c + br
            d2 = tr + c + bl

            if ch(d1) and ch(d2):
                out += 1

    return out

def m(fn):
    with open(fn, "r") as file:
        lines = file.readlines()
    
    print(p1(lines))
    print(p2(lines))

m(sys.argv[1])
