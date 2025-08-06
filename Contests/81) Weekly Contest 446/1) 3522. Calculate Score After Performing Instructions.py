"""
https://leetcode.com/problems/calculate-score-after-performing-instructions
"""


def calculate_score(ins: list[str], vals: list[int]) -> int:
    """"""

    # 1) Optimal (Simulation: While Loop, HashSet): TC = O(n); SC = O(n)

    s = 0
    hs = set()
    i = 0

    while 0 <= i < len(ins) and i not in hs:
        hs.add(i)  # note: needed to be here, because after `if-else`, `i` is updated
        if ins[i] == 'add':
            s += vals[i]
            i += 1
        else:
            i += vals[i]

    return s
