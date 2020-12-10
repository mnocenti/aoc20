#/usr/bin/python

import itertools

# from itertools recipes
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

def part1():
    joltages = [0] + sorted(input) + [max(input)+3]
    diffs = [b-a for a,b in pairwise(joltages)]

    nb_diff_1 = len([d for d in diffs if d == 1])
    nb_diff_3 = len([d for d in diffs if d == 3])
    
    print(nb_diff_1*nb_diff_3)

def memoize(f):
    memo = {}
    def helper(j,i):
        if i not in memo:
            memo[i] = f(j,i)
        return memo[i]
    return helper
    
@memoize
def nb_alternatives(joltages, current_index):
    if current_index == len(joltages)-1:
        return 1
    nb = 0
    current_joltage = joltages[current_index]
    next_index = current_index + 1
    while next_index < len(joltages) and joltages[next_index] <= current_joltage + 3:
        nb += nb_alternatives(joltages, next_index)
        next_index += 1

    return nb

def part2():
    joltages = [0] + sorted(input) + [max(input)+3]
    print(nb_alternatives(joltages, 0))

input = [
    48,
    171,
    156,
    51,
    26,
    6,
    80,
    62,
    65,
    82,
    130,
    97,
    49,
    31,
    142,
    83,
    75,
    20,
    154,
    119,
    56,
    114,
    92,
    33,
    140,
    74,
    118,
    1,
    96,
    44,
    128,
    134,
    121,
    64,
    158,
    27,
    17,
    101,
    59,
    12,
    89,
    88,
    145,
    167,
    11,
    3,
    39,
    43,
    105,
    16,
    170,
    63,
    111,
    2,
    108,
    21,
    146,
    77,
    45,
    52,
    32,
    127,
    147,
    76,
    58,
    37,
    86,
    129,
    57,
    133,
    120,
    163,
    138,
    161,
    139,
    71,
    9,
    141,
    168,
    164,
    124,
    157,
    95,
    25,
    38,
    69,
    87,
    155,
    135,
    15,
    102,
    70,
    34,
    42,
    24,
    50,
    68,
    169,
    10,
    55,
    117,
    30,
    81,
    151,
    100,
    162,
    148,
]

if __name__ == "__main__":
    part1()
    part2()