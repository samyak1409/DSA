"""
https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k
"""


def minimum_partition(s: str, k: int) -> int:
    """"""

    ans = 0
    ss = 0
    for d in s:
        d = int(d)
        if d > k:
            return -1
        ss = ss*10 + d
        if ss > k:
            ans += 1
            ss = d
    return ans + 1
