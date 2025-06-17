"""
https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters
"""


def min_deletion(s: str, k: int) -> int:
    """"""

    # 1) Optimal (Count Freq, Sort): TC = O(n + 26*log2(26)); SC = O(26)
    # We just need to count the freq, sort by freq, and return the sum of frequencies of (total unique - k) least freq
    # chars.

    from collections import Counter

    return sum(sorted(Counter(s).values(), reverse=True)[k:])
