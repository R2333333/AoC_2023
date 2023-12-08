import regex as re
d = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "[1-9]"]
def solve(l:list):
    with open('d1_input') as f:
        s = 0
        for line in f.readlines():
            nums = re.findall('|'.join(l), line, overlapped=True)
            for i in ([0, -1 ] if len(nums) > 1 else [0]):
                nums[i] = l.index(nums[i]) + 1 if not nums[i].isdigit() else int(nums[i])
            s += nums[0] * 10 + nums[-1]
            
        return s
print("Part1: %i\nPart2: %i" % (solve([d[-1]]), solve(d)))
