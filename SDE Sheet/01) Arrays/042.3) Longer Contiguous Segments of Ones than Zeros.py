"""
https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros
"""


def check_zero_ones(s: str) -> bool:
    """"""

    # Modification of https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/042%29%20Max%20Consecutive%20Ones.py.

    # 1) Optimal (Iterate & Track): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/discuss/1228176/Python3-or-Time:-O(n)-or-Space:-O(1)-or-Beats-100-solutions-in-time

    max_streak1 = max_streak0 = streak1 = streak0 = 0  # init
    for char in s:
        if char == '1':
            max_streak1 = max(max_streak1, (streak1 := streak1+1))  # update
            streak0 = 0  # reset
        else:  # (if char == '0')
            max_streak0 = max(max_streak0, (streak0 := streak0+1))  # update
            streak1 = 0  # reset
    return max_streak1 > max_streak0
