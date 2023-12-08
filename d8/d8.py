from math import lcm
convert_all = lambda l, f, arg: [f(_, arg) for _ in l ]

def find(p:str, end):
    s = 0
    while not end(p):
        for i in ins:
            p = d[p][0 if i == 'L' else 1]
            s += 1
            if end(p):
                break
    return s
    
with open('d8_input') as f:
    lines = f.read().splitlines()
    ins, m = lines[0], lines[2:]
    d = {}
    for i in m:
        pos, to = i.split(' = ')
        to = to.split(', ')
        d[pos] = (to[0][1:], to[1][:-1])

    print("part 1: ", lcm(*convert_all(['AAA'], find, lambda x: x == 'ZZZ')))
    print("part 2: ", lcm(*convert_all([_ for _ in d if _[2] == 'A'], find, lambda x: x[2] == 'Z')))
    