import sys
sys.path.append('/Users/royxu/aoc')
from tools.common import *


with open('d8_input') as f:
# with open('example') as f:
    lines = f.read().splitlines()
    ins, m = lines[0], lines[2:]
    d = {}
    for i in m:
        pos, to = i.split(' = ')
        to = to.split(', ')
        d[pos] = (to[0][1:], to[1][:-1])
    pos = 'AAA'
    s = 0
    while pos != 'ZZZ':
        for i in ins:
            pos = d[pos][0 if i == 'L' else 1]
            s += 1
            if pos == 'ZZZ':
                break

    print(s)
    