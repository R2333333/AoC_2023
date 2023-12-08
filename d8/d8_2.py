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
    start_pos = [_ for _ in d if _[2] == 'A']

    def find(p:str):
        s = 0
        pos = p
        while pos[2] != 'Z':
            for i in ins:
                pos = d[pos][0 if i == 'L' else 1]
                s += 1
                if pos == 'ZZZ':
                    break
        return s
    print(lcm(*convert_all(start_pos, find)))
    